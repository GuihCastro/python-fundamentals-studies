# Faça um programa que leia um número qualquer e mostrei o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

print('=' * 50)
print('{:^50}'.format('CÁLCULO DE FATORIAL'))
print('=' * 50)

num = int(input('Informe um número: '))
c = num
result = 1

while c > 0:
    result *= c
    c -= 1

print('O fatorial de {}(!) é: {}.'.format(num, result))
