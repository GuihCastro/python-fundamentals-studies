# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print('{:=^50}'.format(' SOMA DE 6 NÚMEROS PARES '))

s = 0
count = 0

for c in range(1, 7):
    n = int(input('Informe o {}º número inteiro: '.format(c)))
    if n % 2 == 0:
        s += n
        count += 1

print('\nA soma do(s) {} número(s) par(es) informados é: {}.'.format(count, s) if count != 0 else 'Não foram informados números pares.')
