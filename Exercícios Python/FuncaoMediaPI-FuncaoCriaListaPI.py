# Função média de números pares e ímpares de uma lista

def media_pi(x, n):
    pares = []
    ímpares = []
    for i in range(n):
        if x[i] % 2 == 0:
            pares.append(x[i])
        else:
            ímpares.append(x[i])
    média_p = sum(pares) / len(pares)  # Cálculo da média dos números pares
    média_i = sum(ímpares) / len(ímpares)  # Cálculo da média dos números ímpares
    return média_p, média_i


vetor = []
a = int(input('Digite o número de elementos do vetor: '))  # Informar a quantidade de elementos presentes na lista
for k in range(a):
    vetor.append(int(input('Adicione um valor ao vetor: ')))
y, z = media_pi(vetor, a)
media_vetor = sum(vetor) / len(vetor)
print(f'Vetor = {vetor}')
print(f'Média dos números pares = {y}')
print(f'Média dos números ímpares = {z}')
print(f'Média dos números do vetor ={media_vetor}')

# Função cria lista de números pares ou ímpares no intervalo de 0 a 100

import random


def lista_pi(n, t):
    vetor_p = []
    vetor_i = []
    if t == 1:
        for i in range(n):
            vetor_p.append(random.randrange(0, 100, 2))
        return vetor_p
    else:
        for i in range(n):
            vetor_i.append(random.randrange(1, 100, 2))
        return vetor_i


a = int(input('Informe a quantidade de elementos do vetor: '))  # Digitar o número de termos da lista
b = int(input('Digite "1" para criar uma lista de números pares ou "2" para criar uma lista de números ímpares: '))  # Digitar 1 ou 2 para criar o tipo de lista desejada
lista = lista_pi(a, b)  # Colocar entre parênteses as variáveis que irão substituir o n e o t na função, respectivamente
if b == 1:
    print(f'Você escolheu uma lista de números pares, essa foi a lista criada: {lista}')
else:
    print(f'Você escolheu uma lista de números ímpares, essa foi a lista criada: {lista}')