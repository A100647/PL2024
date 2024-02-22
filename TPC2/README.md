# TPC2

**Título:** Desenvolvimento de um Conversor Markdown para HTML  
**Autor:** Martim Quintelas Pinto Félix, A100647  
**Lista de Parágrafos:**  
Este trabalho tem como objetivo a criação de um programa em Python que converte texto formatado em Markdown para HTML. O programa foca-se na conversão de elementos básicos da sintaxe Markdown, permitindo uma representação visual aprimorada em web.

As funcionalidades específicas implementadas no programa incluem:

1. **Conversão de Cabeçalhos**: 
   - Identifica e converte, usando expressões regulares, cabeçalhos Markdown em HTML, suportando três níveis de cabeçalhos (`#`, `##`, `###`).

2. **Formatação de Texto**:
   - Permite a conversão de texto em **negrito** e *itálico*, utilizando as marcações `**texto**` para negrito e `*texto*` para itálico.
   - Utilizo também expressões regulares para realizar estas substituições de forma eficiente.

3. **Listas e Links**:
   - Converte listas numeradas para o formato HTML correspondente, preservando a ordem e a hierarquia dos itens.
   - Transforma links e imagens Markdown (`[texto](URL)`, `![texto alternativo](URL da imagem)`) nos seus equivalentes HTML.

## Descrição do Trabalho Desenvolvido

A implementação do programa envolve a utilização de expressões regulares para identificar padrões específicos na sintaxe Markdown e substituí-los pelo código HTML apropriado.

- **Processamento de Texto**:
  - A função principal analisa o texto de entrada, aplicando várias regras de conversão para gerar o output em HTML.
  - Diferentes padrões são identificados para cada elemento Markdown suportado, sendo cada um tratado por uma expressão regular específica.

- **Implementação Detalhada**:
    - Para cabeçalhos, a deteção e substituição é feita de forma hierárquica, começando com `#` até `###`.
    <br>
    ```python
    markdown_text = re.sub(r'### (.*)', r'<h3>\1</h3>', markdown_text)
    ```
    - Textos em negrito e itálico são convertidos utilizando grupos de captura nas suas expressões regulares correspondentes.
    <br>
    ```python
    markdown_text = re.sub(r'\*\*(.*)\*\*', r'<b>\1</b>', markdown_text)
    ```
    - Para a **inclusão de imagens e links**, são utilizadas expressões regulares específicas que transformam a sintaxe Markdown para as tags HTML `<img>` e `<a>`, respetivamente, mantendo os atributos essenciais como o `href` para links e `src` para imagens.
    <br>
        ```python
        markdown_text = re.sub(r'!\[(.*)\]\((.*)\)', r'<img src="\2" alt="\1"/>', markdown_text)
        markdown_text = re.sub(r'\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', markdown_text)
        ```
  
    - A **implementação para tratar das listas numeradas** envolve uma expressão regular complexa que identifica toda a lista e a converte numa estrutura `<ol>` com vários itens `<li>`. Esta abordagem garante que todas as entradas da lista sejam capturadas como uma unidade e devidamente formatadas.
    <br>
        ```python
            def converter_lista_numerada(match):
                itens_lista = match.group(0).split('\n')
                itens_lista = [item for item in itens_lista if item]
                lista_html = "<ol>" + "".join(f"<li>{item[item.index(' ')+1:]}</li>" for item in itens_lista) + "</ol>"
                return lista_html
            
            markdown_text = re.sub(r'(?m)^\d+\.\s.*(?:\n\d+\.\s.*)*', converter_lista_numerada, markdown_text)
        ```

- **Resultados e Apresentação**:
  - O output final é um documento HTML estruturado com os elementos convertidos, pronto para ser visualizado em um navegador.
  - Este processo não só facilita a leitura e interpretação do texto original como também amplia as possibilidades de formatação e design.

