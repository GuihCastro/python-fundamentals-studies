# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('{:=^50}'.format(' SOMA DE NÚMERO ÍMPARES E MULTIPLOS DE 3 ENTRE 1 E 500 '))

s = 0
count = 0

'''for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        s += c'''

for c in range(3, 501, 3):
    if c % 2 != 0:
        s += c
        count += 1

print('A soma dos {} números ímpares que são múltiplos de 3 e se encontram no intervalo de 1 até 500 é: {}.'.format(count, s))
