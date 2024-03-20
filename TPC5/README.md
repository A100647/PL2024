# TPC2

**Título:** Analisador Léxico para Máquina de Vending  
**Autor:** Martim Quintelas Pinto Félix, A100647
**Lista de Parágrafos:**  
Este projeto centra-se na criação de um analisador léxico em Python, projetado para interagir com uma máquina de vending simulada. Através deste script, é possível interpretar comandos específicos, como listar produtos, inserir moedas, selecionar produtos e terminar a sessão. O programa utiliza expressões regulares para identificar e processar comandos, manipulando o saldo do usuário e o stock de produtos com base na interação.

As funcionalidades específicas implementadas no analisador incluem:

1. **Listar Produtos**:
   - Exibição de todos os produtos disponíveis, incluindo código, nome, quantidade e preço.
   
2. **Inserir Moedas**:
   - Aceitação e processamento de moedas de diferentes valores, atualizando o saldo disponível para compras.

3. **Selecionar Produtos**:
   - Permite ao utilizador selecionar um produto pelo código, verificando se o saldo é suficiente e ajustando o stock conforme necessário.

4. **Terminar Sessão**:
   - Finalização da interação com a máquina de vending, devolvendo o troco se aplicável e encerrando o programa.

## Descrição do Trabalho Desenvolvido

Segue-se uma explicação detalhada do código implementado:

- **Estrutura da Classe MaquinaVending**:
  - Inicialização com stock de produtos e definição de tokens como expressões regulares para capturar comandos específicos (`LISTAR`, `MOEDA`, `SELECIONAR`, `SAIR`).

- **Comandos Implementados**:
  - **LISTAR**:
    Utiliza `tabulate` para formatar e exibir os produtos em stock.
    ```python
    def t_LISTAR(self, t):
        r'LISTAR'
        # Código para listar produtos
    ```
  
  - **MOEDA**:
    Processa várias moedas inseridas, atualizando o saldo do utilizador.
    ```python
    def t_MOEDA(self, t):
        r"MOEDA\s+..."
        # Código para processar moedas
    ```
  
  - **SELECIONAR**:
    Permite ao usuário escolher um produto, verificando saldo e ajustando o stock.
    ```python
    def t_SELECIONAR(self, t):
        r"SELECIONAR\s+..."
        # Código para selecionar produtos
    ```
  
  - **SAIR**:
    Encerra a sessão, devolvendo troco se necessário e terminando o programa.
    ```python
    def t_SAIR(self, t):
        r'SAIR'
        # Código para terminar sessão
    ```

- **Resultados e Apresentação**:
  - Interpretação dos comandos inseridos pelo utilizador, com feedback visual imediato após cada ação.
  - A saída do programa é apresentada diretamente na consola, permitindo uma interação fluida e intuitiva com a máquina de vending simulada.

