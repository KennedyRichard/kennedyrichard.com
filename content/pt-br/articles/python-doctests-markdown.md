authors: Kennedy Richard S. Guerra
author-urls: https://kennedyrichard.com/pt-br
translators: Kennedy Richard S. Guerra
translator-urls: https://kennedyrichard.com
keywords: Python
          doctests de Python
          doctests
          markdown
description: Artigo sobre as vantagens de usar arquivos markdown como doctests de Python
publish-date: 2025-11-17
last-updated: 2026-05-08
include-comment-section: True


# Doctests de Python ricos e expressivos usando markdown

Doctests nos permitem inserir testes diretamente no docstring da unidade sendo testada, como na dosctring de uma função, desse jeito:

```python
def add(a, b):
    """Retorna a soma de dois números.

    >>> add(1, 1)
    2
    >>> add(-1, 1)
    0
    """
    return a + b
```

Manter estes testes atualizados é conveniente porque ele estão localizados o mais próximo possível do código que eles testam.

No entanto, ao menos em minha experiência, outra funcionalidade de doctests que parecem ser muito menos explorado/ensinado: o fato de doctests funcionarem com arquivos de texto de qualquer tipo and poderem ser alocados foram do módulos de Python que eles estão testando. Para ser honesto, o único material que me lembro de já ter visto tocando neste aspecto dos doctests foi o livro do Daniel Arbuckle (em inglês): "Learning Python testing: a straightforward and easy approach to testing your Python projects".

Aqui extendo a abordagem do autor para incluir o uso de arquivos markdown, outro tipo de arquivo de texto que, no entanto, oferece muitas funcionalidades adicionais.


## Doctests em arquivos markdown dedicados

Colocar doctests em seus próprios arquivos de texto dedicados é útil para muitos propósitos diferentes. Por exemplo, se seu código é muito versátil, incrementar as docstrings no seu código pode deixá-las muito longas, fazendo que leitores tenham de rolar um monte de texto antes que cheguem no código em si. E os módulos de Python ficariam enormes.

Usar arquivos de texto dedicados para testes também é útil para testes que são mais compreensivos, testando não apenas unidades, mas também suas interações.

No entanto, o maior valor que você pode extrair dos doctests (dependendo de suas necessidades, é claro) é talvez prover doctests ricos e expressivos por meio do bom uso do format markdown. Você pode criar arquivos markdown dedicados que descrevem e demonstram seu código, incluindo não apenas os testes e o texto explicando eles, mas também: 

- formatação de texto rica (renderizar texto em negrito, itálico, texto tachado/rasurado)
- estrutura de texto (por meio de cabeçalhos para o texto e suas seções/subseções)
- bela renderização (incluindo código com texto realçado)
- mídia (imagens/gifs, vídeo e mais)
- tabelas

A imagem abaixo mostra um arquivo de markdown usado como doctest, que renderiza de forma muito bonita no GitHub e outros visualizadores de markdown:

<img alt="Captura de tela de arquivo markdown usado como doctest renderizado no GitHub, obtido do repositório KennedyRichard/python-markdown-doctests" src="https://i.imgur.com/HEERs16.png" style="border: 1px solid black" />

Nota do tradutor: O texto na imagem apresenta a função `multiply` e explica que os testes demonstram seu uso e comparam seu output com o output da função `operator.mul` (da biblioteca padrão de Python). Logo após essa breve explicação há um bloco de código contendo código Python, que são os testes. O comentário na parte inferior desse bloco de código (as linhas que começam com `#`) apenas diz que como as linhas que começam com `>>>` são tratadas como código Python, você pode incluir comentários nelas, e isso inclui comentários especiais chamados diretivas, que são utilizadas em doctests para acionar condições específicas. Inclusive, na penúltima linha do bloco de código, é possível notar o uso da diretiva `# doctest: +ELLIPSIS`.

Caso tenha curiosidade, a diretiva `# doctest: +ELLIPSIS` vista no bloco de código mostrado na imagem anterior permite que parte do output do teste seja omitido usando os caracteres `...`. Neste caso em específico, utilizamos essa diretiva para não precisarmos prover o id da função `multiply` já que é um detalhe que só teríamos como saber na hora em que o código é carregado e executado pela instância de Python.


## Como funciona

Isto é possível porque a única formatação requerida para doctests é o uso dos caracteres `>>>` para marcar código a ser executado, seguidos por uma linha representando o output daquele código (que deve ser uma linha vazia se o output for `None`).

O `>>>` é às vezes também seguido por uma ou mais linhas com os caracteres `...`, quando o código a ser executado se extende por uma ou mais linhas. Qualquer arquivo de texto que não que não entre em conflito com tal formatação pode portanto ser usado como um doctest, incluindo o markdown.

A única medida adicional requerida quando empregamos markdown como doctests é a de incluir um único pequeno script de Python na mesma pasta (ou próximo) apenas para que você possa importar os objetos/valores para os testes e os arquivos markdown contendo os testes.

Esta medida adicional não é um requerimento exclusivo de arquivos mardown, mas é algo que se aplica a qualquer arquivo de texto que se queira usar como doctest. A razão é que o módulo da biblioteca padrão do Python [unittest](https://docs.python.org/pt-br/3/library/unittest.html) só consegue descobrir automaticamente módulos de Python.

Uma vez que o pequeno script é adicionado próximo aos arquivos markdown, o módulo unittest pode ser usado para descobrir automaticamente tais doctests e executá-los.

Eu criei um repositório GitHub como exemplo com tudo necessário para que você possa ver como tudo funciona e a aparência desses doctests (dê uma olhada nas instruções do README, em inglês): [KennedyRichard/python-markdown-doctests](https://github.com/KennedyRichard/python-markdown-doctests).


## Vá além

Lembre-se: seus doctests não precisam demonstrar somente o uso básico do seu código, mas poderiam também ir além e destravar muitas possibilidades na mentes de quem usa por meio da tomada de tempo e carinho extra para demonstrar tal poder com testes mais detalhados e visualmente agradáveis utilizando o markdown.

Se você fosse incluir todos esses testes adicionais dentro dos seus módulos de Python, nas docstrings de suas definições, os scripts poderiam acabar muito longos e apresentar uma parede de texto antes que quem lê possa inspecionar o próprio código no corpo das definições. 

Doctests de Python em markdown oferecem um ambiente muito mais amigável para exploração e aprendizagem. Eles são renderizados de forma muito bonita e oferecem a possibilidade do uso de elementos visuais para dar suporte/melhorar a aprendizagem.

Eu ainda não explorei a possibilidade a seguir no repositório exemplo que mentionei anteriormente, mas se você acha que é apropriado para seu caso, você pode até mesmo fazer uso de funcionalidades que são exclusivas de ferramentas markdown específicas.

Por exemplo, markdown renderizado no GitHub tem sintaxes adicionais disponíveis para renderização de muitos outros tipos úteis de elementos de texto e/ou visuais, como alertas/admonições, notação matemática, diagramas, etc.

Imagem abaixo mostra como uma pessoa pode renderizar diagramas no GitHub:

<img alt="Captura de tela mostrando texto markdown e o diagrama resultante renderizado no GitHub, tirado da documentação online do GitHub." src="https://i.imgur.com/MYpXdvE.png" style="border: 1px solid black" />

Nota do tradutor: o texto na parte superior da imagem, destacado por um fundo de cor cinza claro, representa texto markdown antes de ser renderizado. A primeira linha representa um parágrafo que diz "Aqui está um simples diagrama de fluxo:", seguido por um bloco de código (o texto delimitado pelos caracteres `...`) cujo conteúdo é um código no formato `mermaid` usado para definir o diagrama. Na metade de baixo da imagem, em fundo branco, é possível ver como o texto markdown foir renderizado no GitHub, isto é, o parágraph que diz "Aqui está..." e o diagrama, que também apresenta controles adicionais para movimentação, zoom e outras funções.

Você pode encontrar mais destes elementos neste link: [https://docs.github.com/pt/get-started/writing-on-github/working-with-advanced-formatting](https://docs.github.com/pt/get-started/writing-on-github/working-with-advanced-formatting).

Isto pode tornar seus doctests ainda mais ricos visualmente e informativos.


## Palavras finais

Como explorado aqui, qualquer arquivo de texto pode ser usado como um doctest de Python. Dada essa possibilidade, você não estaria se perguntando que outros tipos de arquivo de texto poderiam ser úteis também? Que novas possibilidades eles poderiam destravar?

Se você achou este artigo interessante e quer ajudar a manter meu trabalho como um mantenedor de projetos de código aberto, você me encontra no [Patreon](https://patreon.com/KennedyRichard), GitHub [sponsors](https://github.com/sponsors/KennedyRichard), [Apoia-se](https://apoia.se/kennedyrichard) e outros websites como esses que você encontra listados aqui (maior parte em inglês, uma seção em português): [https://indiesmiths.com/donate](https://indiesmiths.com/donate).

