import re

def markdown_para_html(markdown_text):
    
    #Tratar dos cabeçalhos
    markdown_text = re.sub(r'### (.*)', r'<h3>\1</h3>', markdown_text)
    markdown_text = re.sub(r'## (.*)', r'<h2>\1</h2>', markdown_text)
    markdown_text = re.sub(r'# (.*)', r'<h1>\1</h1>', markdown_text)
    
    
    
    #Tratar do bold
    markdown_text = re.sub(r'\*\*(.*)\*\*', r'<b>\1</b>', markdown_text)
    
    #Tratar do italico
    markdown_text = re.sub(r'\*(.*)\*', r'<i>\1</i>', markdown_text)
    
    #Tratar das imagens
    markdown_text = re.sub(r'!\[(.*)\]\((.*)\)', r'<img src="\2" alt="\1"/>', markdown_text)
    
    #Tratar dos links
    markdown_text = re.sub(r'\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', markdown_text)

    #Tratar das listas (H)
    # Encontra todos os itens da lista e converte
    def converter_lista_numerada(match):
        itens_lista = match.group(0).split('\n')
        # Remove strings vazias que podem aparecer devido a novas linhas extras
        itens_lista = [item for item in itens_lista if item]
        lista_html = "<ol>" + "".join(f"<li>{item[item.index(' ')+1:]}</li>" for item in itens_lista) + "</ol>"
        return lista_html
    
    markdown_text = re.sub(r'(?m)^\d+\.\s.*(?:\n\d+\.\s.*)*', converter_lista_numerada, markdown_text)
          
    return markdown_text

def converter_arquivo_md_para_html(arquivo_md, arquivo_html):
    with open(arquivo_md, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    
    html_text = markdown_para_html(markdown_text)
    
    with open(arquivo_html, 'w', encoding='utf-8') as f:
        f.write(html_text)
        
if __name__ == '__main__':
    nome_arquivo_md = 'exemplo.md'
    nome_arquivo_html = 'exemplo.html'
    converter_arquivo_md_para_html(nome_arquivo_md, nome_arquivo_html)