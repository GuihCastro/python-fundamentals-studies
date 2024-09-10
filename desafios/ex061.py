# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('=' * 50)
print('{:^50}'.format('PROGRESSÃO ARITMÉTICA v2.O'))
print('=' * 50)

first = int(input('Informe o primeiro termo da PA: '))
reason = int(input('Informe a razão da PA: '))
t = first
c = 0

while c < 10:
    if c < 9:
        print(t, end=', ')
    else:
        print(t)
    t += reason
    c += 1
