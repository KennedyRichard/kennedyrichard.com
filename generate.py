"""Script for generating Kennedy Richard's static website.

https://kennedyrichard.com
"""

### standard library imports

from pathlib import Path

from shutil import copytree, rmtree

from string import Template

from ast import literal_eval

from datetime import datetime

from warnings import warn


### third-party import
from markdown import Markdown



### constants and module level objs

MANDATORY_PAGE_METADATA = (
    'authors',
    'description',
    'keywords',
)

MANDATORY_POST_METADATA = (
    'publish-date',
    'author-urls',
    *MANDATORY_PAGE_METADATA,
)

meta_in_post_template = Template("""
<ul>

<li>Author(s): $authors</li>
<li>Created: $created</li>
$updated

</ul>
""".strip()
)

md = Markdown(extensions=['meta', 'extra', 'sane_lists'])

get_publish_date = lambda item: item['publish-date'][0]

### grab relevant paths

HERE = Path(__file__).parent
sourcepath = HERE / 'content'
targetpath = HERE / '_output'


### make sure '_output' folder exists and is empty

if targetpath.is_dir():
    rmtree(str(targetpath))

else:
    targetpath.mkdir()

### copy images folder as-is
copytree(str(sourcepath / 'images'), str(targetpath / 'images'))

### grab templates

_templates_dir = sourcepath / '_templates'

page_template = (
    Template(
        (_templates_dir / 'page.html').read_text(encoding='utf-8')
    )
)

post_template = (
    Template(
        (_templates_dir / 'post.html').read_text(encoding='utf-8')
    )
)

redirect_template = (
    Template(
        (_templates_dir / 'redirect.html').read_text(encoding='utf-8')
    )
)



def main():
    """Process contents to generate website."""

    ### iterate over the website content directory generating the .html pages

    for path in sourcepath.iterdir():

        ### ignore paths whose name start with '_' or equals 'images'

        path_name = path.name

        if path_name.startswith('_') or path_name == 'images':
            continue

        ## if path is a .md file, it is a page that must be built

        elif path.suffix.lower() == '.md':

            ## grab content

            content = path.read_text(encoding='utf-8')

            html_text = md.convert(content)
            meta = md.Meta

            missing_keys = tuple(

                key
                for key in MANDATORY_PAGE_METADATA
                if key not in meta

            )

            if missing_keys:

                raise KeyError(
                    f"{path} page missing following keys: {missing_keys}"
                )

            ## prepare data

            page_data = {
                'title': get_title(html_text),
                'authors': get_authors_meta(meta['authors']),
                'description': meta['description'][0],
                'keywords': ', '.join(meta['keywords']),
                'content': html_text,
            }

            final_html_text = page_template.substitute(page_data)

            destination = targetpath / path.with_suffix('.html').name

            ## copy the generated html content to its final destination
            destination.write_text(final_html_text, encoding='utf-8')


        ## if path is a folder, it holds .md posts rather than .html pages
        ##
        ## here we build .html pages for each .md file and a central index.html
        ## page with links to the posts

        elif path.is_dir():

            ## grab folder path and destination

            posts_source = sourcepath / path_name

            posts_dest_dir = targetpath / path_name
            posts_dest_dir.mkdir()

            category_title = path_name.title()

            ## build individual post pages

            posts_meta = []

            for post_path in posts_source.iterdir():

                ###

                extension = post_path.suffix.lower()

                if extension != '.md':

                    warn(
                        f"Posts must be .md file, not {extension} file.",
                        category=RuntimeWarning,
                    )

                    continue

                ###

                post_dest_path = (
                    posts_dest_dir
                    / post_path.with_suffix('.html').name
                )

                post_html = md.convert(post_path.read_text(encoding='utf-8'))
                post_meta = md.Meta

                missing_keys = tuple(

                    key
                    for key in MANDATORY_POST_METADATA
                    if key not in post_meta

                )

                if missing_keys:

                    raise KeyError(
                        f"{post_path} post missing following keys:"
                        f" {missing_keys}"
                    )

                post_title = get_title(post_html)
                post_meta['title'] = post_title
                post_meta['urlname'] = post_dest_path.name

                posts_meta.append(post_meta)

                post_html = insert_meta_into_post(post_meta, post_html)

                post_data = {

                    'category_title': category_title,
                    'title': post_title,
                    'article': post_html,

                }

                final_post_text = post_template.substitute(post_data)

                post_page_data = {
                    'title': post_title,
                    'authors': get_authors_meta(post_meta['authors']),
                    'description': post_meta['description'][0],
                    'keywords': ', '.join(post_meta['keywords']),
                    'content': final_post_text,
                }

                ###

                final_html_content = page_template.substitute(post_page_data)
                post_dest_path.write_text(final_html_content, encoding='utf-8')

            ### build index page for posts

            posts_meta.sort(key=get_publish_date, reverse=True)

            posts_index_html = f'<h1>{category_title}</h1>\n\n<ul>\n\n'

            for post_meta in posts_meta:

                pdate = format_date(post_meta['publish-date'][0])

                title = post_meta['title']
                urlname = post_meta['urlname']

                posts_index_html += (
                    f'<li>{pdate} - <a href="{urlname}">{title}</a>'
                )

                description = post_meta['description'][0]

                posts_index_html += f': {description}.'

                if 'last-updated' in post_meta:

                    ldate = format_date(post_meta['last-updated'][0])
                    posts_index_html += f' (last updated: {ldate})'

                posts_index_html += '</li>\n'

            posts_index_html += '\n</ul>'

            ## write index

            page_data = {
                'title': category_title,
                'authors': get_authors_meta(['Kennedy Richard S. Guerra']),
                'description': f"Chronological pieces in the {path_name} category",
                'keywords': ', '.join({f'{path_name}', 'pieces', 'articles'}),
                'content': posts_index_html,
            }

            final_html_text = page_template.substitute(page_data)

            (
                posts_dest_dir
                / 'index.html'
            ).write_text(final_html_text, encoding='utf-8')


    ### grab and process redirections

    ## redirection data

    redirections_data = (
        literal_eval(
            (sourcepath / '_redirections.pyl').read_text(encoding='utf-8')
        )
    )

    ## process each item

    for key, value in redirections_data.items():

        ## prepare data
        html_content = redirect_template.substitute(link=value)

        ## prepare/define destination

        subdirpath = targetpath / key
        subdirpath.mkdir()

        content_destination = subdirpath / 'index.html'

        ## copy the generated html content to its final destination
        content_destination.write_text(html_content, encoding='utf-8')


### helper functions

def format_date(date_str):

    return (
        datetime
        .strptime(date_str, '%Y-%m-%d')
        .strftime('%Y, %B %d')
    )

def get_title(html_text):

    return html_text[
        html_text.index('<h1>') + 4
        : html_text.index('</h1>')
    ]

def get_authors_meta(authors):

    return '\n'.join(
        f'  <meta name="author" content="{author}" />'
        for author in authors
    )

def get_post_authors(authors, urls):

    return ', '.join(

        f'<a href="{url}">{author}</a>'
        for author, url in zip(authors, urls)

    )

def insert_meta_into_post(post_meta, post_html):

    authors = get_post_authors(
                  post_meta['authors'],
                  post_meta['author-urls'],
              )

    created = format_date(post_meta['publish-date'][0])

    updated = (

        (
            '<li>Last updated: '
            + format_date(post_meta['last-updated'][0])
            + '</li>'
        )
        if 'last-updated' in post_meta
        else ''
    )

    meta_content = meta_in_post_template.substitute(
        authors=authors,
        created=created,
        updated=updated,
    )

    metalines = meta_content.splitlines()
    metalines.reverse()

    lines = post_html.splitlines()

    for i, line in enumerate(lines):
        if '<h1>' in line:
            break

    for line in metalines:
        lines.insert(i+1, line)

    return '\n'.join(lines)



if __name__ == '__main__':
    main()
