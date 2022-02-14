# Função progressão geométrica

def pg(n):
    lista = []
    for x in range(n):
        y = 2 ** x
        lista.append(y)
    soma = sum(lista)
    return soma


a = int(input('Digite o número de termos da progressão geométrica: '))  # Digitar o número de termos para a soma ser efetuada
soma_PG = pg(a)  # Colocar entre parênteses a variável que irá substituir o n da função
print(soma_PG)

# Função soma de números ímpares de um intervalo

def soma_impar(k, n):
    ímpares = []
    for x in range(k, n):
        if x % 2 != 0:
            ímpares.append(x)
    soma = sum(ímpares)
    return soma


a = int(input('Informe o início do intervalo: '))  # Digitar o valor mínimo dos números ímpares
b = int(input('Informe o término do intervalo: '))  # Digitar o valor máximo dos números ímpares
soma_intervalo = soma_impar(a, b)  # Colocar entre parênteses as variáveis que irão substituir o k e o n da função, respectivamente
print(soma_intervalo)