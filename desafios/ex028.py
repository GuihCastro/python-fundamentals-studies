# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('=' * 50)
print('Vou pensar num número entre 0 e 5. Tente adivinhar.')
print('=' * 50)

num = randint(0, 5)
guess = int(input('Em que número eu pensei? '))

print('Será...?')
sleep(2)

if guess == num:
    print('Parabéns! Você acertou!')
else:
    print('Errado! Tente novamente.')
