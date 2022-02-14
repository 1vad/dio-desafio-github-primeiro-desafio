# Equação com 3 valores

def equacao(a, b, c):
    z = (a + b + c) / 3 - (a + b) / 2 + 2
    print(z)
    return z
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
equacao(a, b, c)

# Determinação da faixa etária

def faixa_etaria():
    faixa = 0
    i = int(input('Digite a sua idade: '))
    if i <= 19:
        faixa = 'Jovem'
    if i > 19 and i < 60:
        faixa = 'Adulto'
    if i >= 60:
        faixa = 'Idoso'
    print(f'A faixa etária da sua idade {i} é: {faixa}')
    return faixa
faixa_etaria()