authors: Kennedy Richard S. Guerra
author-urls: https://kennedyrichard.com
keywords: about
          about me
description: Rich and expressive python doctests with markdown
publish-date: 2025-11-17
include-comment-section: True


# Rich and expressive Python doctests with markdown

Doctests allow us to insert tests directly in the docstring of the unit being tested, like in a function's docstring, like this:

```python
def add(a, b):
    """Return the sum of two given numbers.

    >>> add(1, 1)
    2
    >>> add(-1, 1)
    0
    """
    return a + b
```

Maintaining these tests is convenient because they are located as close as possible to the code they test.

However, at least in my experience, another feature of doctests seem to be much less explored/taught: the fact that doctests work with any plain text format and can be placed outside the Python modules they are testing. To be honest, the only material I ever recall having touched on this aspect of doctests was Daniel Arbuckle's book: "Learning Python testing: a straightforward and easy approach to testing your Python projects". Here I extend the author's approach to include the usage of markdown files, another plain text format, but which offers many additional features.

Putting doctests in their own dedicated text files is useful for several different purposes. For instance, if your code is very versatile, populating the docstrings in your code could leave them bloated, requiring readers to scroll past a lot of text before they can reach the actual code. And the Python modules would get too large. Using dedicated text files for tests are also useful for tests that are more comprehensive, testing not only individual units, but their interactions as well.

However, the highest value you can extract from doctests (depending on your needs, of course) is perhaps providing rich and expressive doctests by making good usage of the markdown format. You can create dedicated markdown files describing and demonstrating your code, including not only the tests and the text explaining them, but also:

- rich formatting of the text (rendering text in bold, italics, strikethrough styles)
- structure for the text (via headings)
- beautiful rendering (including code highlighting)
- media (images/gifs, video and more)
- tables

The image below depicts a doctest markdown file like that, which renders beautifully on GitHub and other markdown viewers:

<img alt="Screenshot of markdown doctest rendered on GitHub, from KennedyRichard/python-markdown-doctests repository" src="https://i.imgur.com/HEERs16.png" style="border: 1px solid black" />

This is possible because the only formatting required by doctest is the usage of the `>>>` characters to mark code to be executed, followed by a line representing the output of that code (which must be empty, if the output is `None`). The `>>>` is sometimes also followed by one or more lines with `...` characters, when the code to be executed extends to one or more lines. Any format that doesn't conflict with such formatting can thus be used as a doctest, including markdown.

The only additional measure required when employing markdown as doctests is to include a single small python script in the same folder (or near it) just so you can import the required objects/values for the tests and the markdown files containing the tests.

This additional measure is not a requirement exclusive to markdown files, but it is required in order to use any plain text format as a doctest. The reason is that the standard library's module [unittest](https://docs.python.org/3/library/unittest.html) can only discover Python modules automatically.

Once the small script is added near the markdown files, the unittest module can be used to automatically discover such doctests and execute them.

I created an example GitHub repository with everything setup so you can see how it all works and looks (check the README for instructions): [KennedyRichard/python-markdown-doctests](https://github.com/KennedyRichard/python-markdown-doctests).

Remember: your doctests don't need to demonstrate only the basic usage of your code, but instead you can also go further and unlock many possibilities in the minds of your users by taking the extra time and care to demonstrate such power with more detailed and visually pleasing tests with markdown.

If you were to include all those additional tests inside your Python modules, in the docstrings of your definitions, the scripts could end up bloated and present a wall of text before a user could inspect the actual code in the bodies of the definitions. Python markdown doctests offer a much more friendly environment for exploration and learning. They are beautifully rendered and offer the possibility of using visual elements to support/improve learning.
