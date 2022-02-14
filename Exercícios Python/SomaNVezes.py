# Soma dois números n vezes

n = int(input('Digite o valor de N: '))
for i in range(n):
    print('Digite os valores de X e Y: ')
    x = float(input())
    y = float(input())
    z = x + y
    print(f'X = {x}, Y = {y}, Soma = {z}')
print('='*15, 'FIM', '='*15)