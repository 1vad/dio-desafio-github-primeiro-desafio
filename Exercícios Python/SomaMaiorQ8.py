# Soma números maiores que 8 do vetor

x = [5, 12, 7, 8, 4, 6, 11, 20, 23, 2, 14, 17]
n = 12
soma = 0
for i in range(0, n):
    if x[i] > 8:
        soma = soma + x[i]
print(f'Vetor = {x}\nValor da soma = {soma}')