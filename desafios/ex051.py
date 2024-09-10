# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 50)
print('{:^50}'.format('10 PRIMEIROS TERMOS DA PA'))
print('=' * 50)

first = int(input('Informe o primeiro termo da PA: '))
reason = int(input('Informe a razão da PA: '))
n = first

for c in range(0, 10):
    print(n, end=', ')
    n += reason

print('FIM')
