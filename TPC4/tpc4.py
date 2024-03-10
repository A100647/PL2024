import re

# Define os tokens como expressões regulares
TOKENS = [
    (r'[ \t]+', None),  # Ignora espaços e tabs
    (r'[,]', 'COMMA'),
    (r'Select', 'SELECT'),
    (r'From', 'FROM'),
    (r'Where', 'WHERE'),
    (r'>=', 'GE'),
    (r'<=', 'LE'),
    (r'=', 'EQ'),
    (r'>', 'GT'),
    (r'<', 'LT'),
    (r'[0-9]+', 'NUMBER'),
    (r'[a-zA-Z_][a-zA-Z_0-9]*', 'IDENTIFIER'),  # Identificadores
]

def tokenize(input_string):
    tokens = []
    while input_string:
        match = None
        for token_regex, token_type in TOKENS:
            regex = re.compile(token_regex)
            match = regex.match(input_string)
            if match:
                text = match.group(0)
                if token_type:
                    tokens.append((token_type, text))
                break
        if not match:
            raise SyntaxError(f"Syntax error: {input_string}")
        else:
            input_string = input_string[match.end():]
    return tokens

# Exemplo de uso
query = "Select id, nome, salario From empregados Where salario >= 820"
tokens = tokenize(query)
for token in tokens:
    print(token)
