# Função que calcula a soma das potências de um número com o expoente 1 até N

def potencias(b, c):
    a = 0
    for i in range(1, b + 1):
        a = a + c ** i
    return a
X = int(input('Digite um valor: '))  # Digitar o valor que será usado para calcular a soma: x + x² + x³ + x^4 +. . . + x^n
N = int(input('Digite o número de termos da soma: '))
soma = potencias(N, X)  # Colocar entre parênteses os elementos que vão substituir as variáveis b e c na função, respectivamente
print(f'A soma calculada é: {soma}')

# Função que cria uma lista com o quadrado dos valores digitados

def lista_quad(a):
    lista2 = []
    for i in range(len(a)):
        lista2.append(a[i] ** 2)
    return(lista2)
lista1 = []
n = int(input('Digite o número de termos da lista: '))  # Digitar a quantidade de números que a lista1 terá
for i in range(n):
    z = int(input('Adicione um valor à lista: '))  # Digitar cada valor da lista1
    lista1.append(z)
quadrados = lista_quad(lista1)  # Colocar entre parênteses o elemento que vai substituir a variável a na função
print(f'Essa é a lista com os quadrados dos valores digitados anteriormente: {quadrados}')