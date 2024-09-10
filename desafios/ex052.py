# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('=' * 50)
print('{:^50}'.format('IDENTIFICADOR DE NÚMEROS PRIMOS'))
print('=' * 50)

n = int(input('Informe um número inteiro para saber se ele é primo: '))
is_prime = True

if n <= 1:
    is_prime = False
else:
    for c in range(2, n):
        if n % c == 0:
            is_prime = False
            break

if is_prime:
    print('O número {} \033[32mÉ PRIMO\033[m.'.format(n))
else:
    print('O número {} \033[31mNÃO\033[m é primo.'.format(n))
