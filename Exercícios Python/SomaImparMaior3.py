# Soma números ímpares maiores que 3 do vetor

x = [5, 12, 7, 8, 4, 6, 11, 20, 23, 2, 14, 17, 1, 18]
soma = 0
for i in range(len(x)):
    if x[i] > 3 and x[i] % 2 != 0:
        soma = soma + x[i]
print('Vetor =', x)
print('Soma calculada =', soma)