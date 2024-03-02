# TPC3

**Título:** Somador de Sequências Numéricas em Textos  
**Autor:** Martim Quintelas Pinto Félix, A100647  
**Lista de Parágrafos:**  
Este trabalho concentra-se no desenvolvimento de um script em Python destinado à análise e processamento de texto, com o objectivo de somar todas as sequências de dígitos identificadas. O programa tem a capacidade de alternar o seu comportamento de soma com base na presença das palavras "On" e "Off", independentemente da forma como estas são escritas (maiúsculas ou minúsculas) e apresenta o resultado acumulado das somas sempre que é encontrado o carácter "=".

As funcionalidades específicas implementadas incluem:

1. **Soma de Dígitos**:
   - Identificação e soma de todas as sequências numéricas presentes no texto.

2. **Controlo do Estado de Soma**:
   - Activação e desactivação da soma mediante as palavras "On" e "Off".

3. **Exibição dos Resultados**:
   - Apresentação do total acumulado das somas ao encontrar o carácter "=".

## Descrição do Trabalho Desenvolvido

Segue-se uma descrição detalhada das componentes principais do código implementado:

- **Detalhes da Implementação**:
  - **Deteção e Soma de Números**: A aplicação de expressões regulares permite a identificação de sequências de dígitos no texto, somando os valores detectados sempre que o estado activo (On) está habilitado.
    ```python
    patterns = [
        r"(?P<number>[+-]?\d+)",    # Captura de números inteiros, positivos ou negativos
        r"(?P<activate>on)",        # Captura da palavra 'on', que indica activação
        r"(?P<deactivate>off)"      # Captura da palavra 'off', que indica desactivação
        r"(?P<calculate>=)"         # Captura do sinal de igual, que indica que a soma deve ser apresentada
    ]
    ```

  - **Gestão da Activação/Desactivação**: Alteração do estado de processamento com base na detecção das palavras "On" e "Off", controlando assim a execução das somas.
    ```python
    for line in sys.stdin:
        for match in re.finditer(combined_patterns, line):
            if match.lastgroup == 'activate':
                processing_enabled = True
            elif match.lastgroup == 'deactivate':
                processing_enabled = False
    ```

  - **Apresentação dos Resultados**: A descoberta do carácter "=" desencadeia a exibição do resultado da soma acumulada, reflectindo o total das sequências numéricas processadas até esse momento.
    ```python
    elif match.lastgroup == 'calculate':
        print("Total = " + str(total))
    ```

- **Resultados e Apresentação**:
  - A saída do script é direccionada para a consola, onde o resultado das somas é exibido de forma clara, facilitando a sua leitura e interpretação.
  - Este script demonstra uma utilização eficiente das expressões regulares e da leitura de entrada padrão em Python, reflectindo competências essenciais na programação e no processamento de texto.

