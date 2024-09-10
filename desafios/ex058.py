# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

print('=' * 50)
print('{:^50}'.format('JOGO DA ADIVINHAÇÃO v2.O'))
print('{:^50}'.format('Vou pensar num número entre 0 e 10. Tente adivinhar.'))
print('=' * 50)

from random import randint
from time import sleep

num = randint(0, 10)
guess = int(input('Em que número eu pensei? '))
guesses = 1

print('Será', end='')
sleep(.5)
print('.', end='')
sleep(.5)
print('.', end='')
sleep(.5)
print('.', end='')
sleep(.5)
print('?')
sleep(.5)

while guess != num:
    print('\033[31mERRADO!\033[m')
    if guess < num:
        guess = int(input('Tente um número MAIOR: '))
    else:
        guess = int(input('Tente um número MENOR: '))
    guesses += 1

    print('Será',end='')
    sleep(.5)
    print('.', end='')
    sleep(.5)
    print('.', end='')
    sleep(.5)
    print('.', end='')
    sleep(.5)
    print('?')
    sleep(.5)

print('\033[32mParabéns!\033[m Você acertou!')
print('De primeira!' if guesses == 1 else 'Foram necessárias {} tentativas.'.format(guesses))
