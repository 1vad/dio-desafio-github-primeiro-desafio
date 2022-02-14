# Função soma de números inteiros de 1 a N

def somaN(N, soma):
    soma = 0  # Variável da soma dos valores anteriores a N
    for x in range(1, N):
        soma = soma + x
    return soma
a = int(input('Digite um número: '))
b = int
soma = somaN(a, b)  # Colocar entre os parênteses as variáveis que substituirão as variáveis N e soma da função, respectivamente
print(f'A soma dos valores anteriores a {a} é: {soma}')

# Função soma entre o quadrado de dois valores

def soma_quadrados(X, Y):
    soma = X ** 2 + Y ** 2
    return soma
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
somaQ = soma_quadrados(a, b)  # Colocar entre os parênteses as variáveis que substituirão as variáveis X e Y, respectivamente
print(f'A soma dos quadrados de {a} e de {b} é: {somaQ}')