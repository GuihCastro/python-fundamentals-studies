# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quanto o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

print('=' * 50)
print('{:^50}'.format('TRATANDO VÁRIOS VALORES v1.O'))
print('=' * 50)

from time import sleep

n = q = s = 0 # número, quantidade e soma

while n != 999:
    n = int(input('Informe um número inteiro para ser computado, ou "999" para parar: '))
    if n != 999:
        q += 1
        s += n
    else:
        print('Computando os resultados', end='')
        sleep(.5)
        print('.', end='')
        sleep(.5)
        print('.', end='')
        sleep(.5)
        print('.')
        sleep(.5)

print('Você digitou um total de {} números, e o resultado da soma de todos ele é: {}.'.format(q, s))
