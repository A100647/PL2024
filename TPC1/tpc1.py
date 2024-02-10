import sys

def ParseLinha(linha): # Recebe uma linha de comando e retorna os valores separados por vírgula
    parametros = linha.strip().split(',')
    return parametros[5], parametros[8], parametros[12]

def principal():
    modalidades = []    # Lista de modalidades
    idades = []        # Lista de idades
    total = 0
    aptos = 0
    next(sys.stdin)     # Ignora a primeira linha
    escaloes = {        # Dicionário para os escalões de idade
    '[20-24]' : 0,
    '[25-29]' : 0,
    '[30-34]' : 0,
    '[35-39]' : 0,
}
    for linha in sys.stdin:
        idade_str , modalidade , apto = ParseLinha(linha) # Guarda todas as informações
        if apto == 'true':
            aptos += 1
        total += 1   # Para a percentagem de aptos e inaptos
##########################################################################
        modalidades.append(modalidade)
        modalidades_unicas = sorted(set(modalidades))  # Transformar num conjunto para eliminar repetidos e ordenado
##########################################################################  
        idades.append(int(idade_str)) # Guarda a idade na lista criada e transforma a string em inteiro
    for idade in idades:
        if 20 <= idade <= 24:
            escaloes['[20-24]'] += 1
        elif 25 <= idade <= 29:
            escaloes['[25-29]'] += 1
        elif 30 <= idade <= 34:
            escaloes['[30-34]'] += 1
        elif 35 <= idade <= 39:
            escaloes['[35-39]'] += 1
##########################################################################

#Processar informações
    aptos_final = (aptos / total) * 100 
    inaptos_final = 100 - aptos_final    
    modalidades_unicas = sorted(set(modalidades))  # Transformar num conjunto para eliminar repetidos e ordenado
    
# Resultados 
    for modalidade in modalidades_unicas:
        print(modalidade)
    print(f"{aptos_final:.1f}% aptos")
    print(f"{inaptos_final:.1f}% inaptos")
    for escalao, contador in escaloes.items():
        print(f"{escalao}: {contador}")
        

if __name__ == '__main__':
    principal()