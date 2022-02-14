# Soma maior número

print('='*35)
x = int(input('Digite o valor de x: '))
print('Digite dois valores abaixo: \nDigite 0 para o primeiro número para finalizar o programa.')
v1 = int(input())
v2 = int(input())
while v1 > 0:
    if v1 > v2:
        x = v1 + x
        print('Valor =', x)
    else:
        x = v2 + x
        print('Valor =', x)
    print('Digite mais dois valores abaixo: ')
    v1 = int(input())
    v2 = int(input())
print('='*15, 'FIM', '='*15)