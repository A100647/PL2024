# TPC2

**Título:** Analisador Léxico para Linguagem de Query Simplificada  
**Autor:** Martim Quintelas Pinto Félix, A100647
**Lista de Parágrafos:**  
Este projecto envolve o desenvolvimento de um analisador léxico em Python, desenhado para interpretar e analisar uma linguagem de query simplificada. Através desta script, é possível decompor frases de query, como "Select id, nome, salario From empregados Where salario >= 820", em tokens léxicos, facilitando a sua análise e processamento subsequente. Este analisador léxico é capaz de reconhecer palavras-chave, identificadores, operadores e números, sem a necessidade de recorrer a bibliotecas externas para o processamento de linguagens de query.

As funcionalidades específicas implementadas no analisador incluem:

1. **Reconhecimento de Palavras-chave**:
   - Identificação de *keywords* específicas da linguagem, como "Select", "From" e "Where".

2. **Identificação de Identificadores e Números**:
   - Reconhecimento de identificadores (como nomes de campos e tabelas) e números presentes na query.

3. **Deteção de Operadores**:
   - Identificação de operadores, incluindo operadores de comparação (>, <, >=, <=, =).

4. **Ignorar Espaços em Branco**:
   - Espaços e tabs são ignorados durante a análise, não sendo considerados como tokens.

## Descrição do Trabalho Desenvolvido

Segue-se uma descrição detalhada das principais partes do código implementado:

- **Detalhes da Implementação**:
  - **Definição dos Tokens**: Os tokens são definidos através de expressões regulares, cada uma associada a um tipo de token específico da linguagem de query.
    ```python
    TOKENS = [
        (r'[ \t]+', None),  # Ignora espaços e tabs
        (r'Select', 'SELECT'),
        (r'From', 'FROM'),
        # Resto dos tokens...
    ]
    ```

  - **Processamento da Entrada**: A string de entrada é analisada sequencialmente, à procura de correspondências com as expressões regulares definidas, e cada correspondência é classificada como um token reconhecível.
    ```python
    def tokenize(input_string):
        tokens = []
        # Lógica de tokenização...
        return tokens
    ```

  - **Reconhecimento de Tokens**: Para cada parte da string de *input* que corresponde a uma expressão regular, é criado um token, que é adicionado a uma lista de tokens reconhecidos, excepto para espaços em branco que são ignorados.
    ```python
    for token_regex, token_type in TOKENS:
        match = regex.match(input_string)
        # Lógica de reconhecimento...
    ```

- **Resultados e Apresentação**:
  - A saída do programa consiste numa lista de tokens identificados na string de entrada, cada um com o seu tipo correspondente, facilitando a análise e o processamento posterior da query.



