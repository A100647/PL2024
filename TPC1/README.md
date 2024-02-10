# TPC1 

**Título:** Análise de dados desportivos em linguagem Python  
**Autor:** Martim Quintelas Pinto Félix, A100647  
**Lista de Parágrafos:**  
O objetivo deste trabalho é desenvolver um programa em Python capaz de ler e processar dados de um dataset sobre atletas sem recorrer ao módulo CSV.  
As tarefas específicas a serem executadas pelo programa incluem:

1. **Listagem das Modalidades Desportivas**: 
   - Extrair todas as modalidades desportivas presentes no dataset.
   - Apresentar estas modalidades numa lista alfabeticamente ordenada.

2. **Cálculo da Percentagens de Aptidão**:
   - Determinar a percentagem de atletas aptos e inaptos para a prática desportiva.
   - Este cálculo visa refletir a proporção de atletas cuja condição física os qualifica ou desqualifica para a prática desportiva.

3. **Distribuição por Escalão Etário**:
   - Organizar os atletas em escalões etários definidos em intervalos de cinco anos.
   - Categorizar cada atleta num determinado escalão, com base na sua idade, e apresentar a distribuição total de atletas por estes escalões.
   - Esta análise permite uma compreensão aprofundada da composição etária dos atletas, oferecendo insights sobre as faixas etárias mais representadas.

## Descrição do Trabalho Desenvolvido

O trabalho consiste na implementação de um programa Python projetado para processar um conjunto de dados desportivos lidos através do `stdin`.

- **Extração de Dados**: A função `ParseLinha` analisa cada linha do input, extraindo informações sobre a idade, modalidade desportiva e aptidão física do atleta.
- **Análise dos Dados**: O programa processa estas informações para:
  - Listar alfabeticamente as modalidades desportivas, removendo duplicados com a linha `modalidades_unicas = sorted(set(modalidades))`.

  - Calcular as percentagens de atletas aptos e inaptos.
    ```python
    aptos_final = (aptos / total) * 100 
    inaptos_final = 100 - aptos_final
    ```
  - Agrupar atletas por escalões etários, apresentando a distribuição etária.
    ```python
    for idade in idades:
        if 20 <= idade <= 24:
            escaloes['[20-24]'] += 1
        elif 25 <= idade <= 29:
            escaloes['[25-29]'] += 1
        elif 30 <= idade <= 34:
            escaloes['[30-34]'] += 1
        elif 35 <= idade <= 39:
            escaloes['[35-39]'] += 1
    ```

- **Apresentação dos Resultados**: Os resultados são apresentados de forma clara e concisa no terminal, destacando as modalidades desportivas, as percentagens de aptidão, e a distribuição etária dos atletas.

Esta abordagem não só permite uma análise detalhada e organizada dos dados desportivos mas também promove a eficiência do código através do uso estratégico de estruturas de dados como listas, conjuntos e dicionários.


