# Transforma o comando while abaixo em um comando for equivalente:
# t=0
# x=1
# while x <= 5:
# t = t + x
# x = x + 1
# print("Valor = ", t)

t = 0
x = 1
for x in range(6):
    t = t + x
    x = x + 1
print('Valor =', t)
