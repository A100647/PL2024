# TPC2

**Título:** Conversor de Markdown para HTML em Python  
**Autor:** Martim Quintelas Pinto Félix
**Lista de Parágrafos:**  
Este trabalho foca-se no desenvolvimento de um programa em Python capaz de converter texto originalmente em Markdown para HTML. A implementação abrange a conversão de cabeçalhos, texto em negrito e itálico, imagens, links e listas numeradas sem utilizar bibliotecas externas para o processamento de Markdown.

As tarefas específicas realizadas pelo programa incluem:

1. **Conversão de Cabeçalhos**: 
   - Identificar e converter cabeçalhos de diferentes níveis, marcados com `#`, `##`, ou `###`.
   
2. **Formatação de Texto**:
   - Converter texto em negrito e itálico, utilizando os símbolos `**` e `*`, respetivamente.

3. **Inclusão de Imagens e Links**:
   - Converter sintaxe Markdown para tags HTML que permitem incluir imagens e links na página web.

4. **Criação de Listas Numeradas**:
   - Identificar listas numeradas no texto Markdown e convertê-las para listas ordenadas em HTML.

## Descrição do Trabalho Desenvolvido

A implementação detalhada do programa é apresentada a seguir:

- **Implementação Detalhada**:
  - Para **cabeçalhos**, a deteção e substituição é realizada de forma hierárquica, iniciando com `#` até `###`, garantindo a correta conversão para os correspondentes cabeçalhos HTML (`<h1>` até `<h3>`).
    ```python
    markdown_text = re.sub(r'### (.*)', r'<h3>\1</h3>', markdown_text)
    markdown_text = re.sub(r'## (.*)', r'<h2>\1</h2>', markdown_text)
    markdown_text = re.sub(r'# (.*)', r'<h1>\1</h1>', markdown_text)
    ```
  
  - **Textos em negrito e itálico** são convertidos utilizando expressões regulares que capturam os grupos de texto correspondentes, permitindo a substituição direta pela formatação HTML desejada (`<b>` para negrito e `<i>` para itálico).
    ```python
    markdown_text = re.sub(r'\*\*(.*)\*\*', r'<b>\1</b>', markdown_text)
    markdown_text = re.sub(r'\*(.*)\*', r'<i>\1</i>', markdown_text)
    ```
  
  - Para a **inclusão de imagens e links**, são utilizadas expressões regulares específicas que transformam a sintaxe Markdown para as tags HTML `<img>` e `<a>`, respetivamente, mantendo os atributos essenciais como o `href` para links e `src` para imagens.
    ```python
    markdown_text = re.sub(r'!\[(.*)\]\((.*)\)', r'<img src="\2" alt="\1"/>', markdown_text)
    markdown_text = re.sub(r'\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', markdown_text)
    ```
  
  - A **implementação para tratar das listas numeradas** envolve uma expressão regular complexa que identifica toda a lista e a converte numa estrutura `<ol>` com vários itens `<li>`. Esta abordagem garante que todas as entradas da lista sejam capturadas como uma unidade e devidamente formatadas.
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

