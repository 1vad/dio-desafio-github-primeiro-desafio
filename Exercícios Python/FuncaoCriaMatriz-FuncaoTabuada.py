# Função cria matriz e vetor com números divisíveis por 3 e menores que 15

def cria_matriz(mat, m, n):  # mat = matriz    m = número de linhas    n = número de colunas
    vetor = []
    for l in range(m):
        linha = []
        for c in range(n):
            x = int(input(f'Adicione um valor à matriz na posição ({l + 1},{c + 1}): '))  # Digitar o valor que entrará na matriz na posição apresentada
            linha.append(x)
        mat.append(linha)
    for m in mat:
        for x in m:
            print(f'[{x:^5}]', end='\t')  # Impressão da função
            if x % 3 == 0 and x < 15:
                vetor.append(x)
        print()
    return vetor


matriz = []
linhas = int(input('Digite o número de linhas da matriz: '))  # Informar o número de linhas da matriz a ser criada
colunas = int(input('Digite o número de colunas da matriz: '))  # Informar o número de colunas da matriz a ser criada
z = cria_matriz(matriz, linhas,
         colunas)  # Colocar entra parênteses os elementos que irão substituir as variáveis mat, m e n, respectivamente
print(f'Vetor criado: {z}')

# Função lista da tabuada de um número

def lista_tabuada(k, n):  # k = número a ser multiplicado   n = número de elementos da lista
    lista = []
    x = 0
    for i in range(1, n + 1):
        x = k * i
        lista.append(x)
    return lista


a = int(input('Digite um valor: '))  # Escolher um valor a ser multiplicado
b = int(input('Digite até qual número você deseja multiplicar o valor anterior: '))  # Informar até que número, que será também a quantidade de números da lista, o valor a será multiplicado
l = lista_tabuada(a, b)  # Colocar entre parênteses os valores que substituirão as variáveis k e n da função, respectivamente
print(f'Lista criada: {l}')