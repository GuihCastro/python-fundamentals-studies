# Crie um programa que faça o computador jogar Jokenpô com você.

print('\033[33m~\033[m' * 30)
print('\033[34mVAMOS JOGAR JOKENPÔ!\033[m')
print('\033[33m~\033[m' * 30)

from random import choice
from time import sleep

jokenpo = ('Pedra', 'Papel', 'Tesoura')
pc = choice(jokenpo)
user = str(input('Faça a sua escolha digitando "\033[35mPEDRA\033[m", "\033[35mPAPEL\033[m" ou "\033[35mTESOURA\033[m": '))

print('\nJO')
sleep(.5)
print('KEN')
sleep(.5)
print('PÔ!!!')
sleep(.5)

print('\nO computador jogou {}.'.format(pc.upper()))

if user.lower() == 'pedra':
    if pc.lower() == 'pedra':
        print('\033[33mEMPATE!\033[m')
    elif pc.lower() == 'papel':
        print('\033[31mDERROTA!\033[m')
    else:
        print('\033[32mVITÓRIA!\033[m')
elif user.lower() == 'papel':
    if pc.lower() == 'pedra':
        print('\033[32mVITÓRIA!\033[m')
    elif pc.lower() == 'papel':
        print('\033[33mEMPATE!\033[m')
    else:
        print('\033[31mDERROTA!\033[m')
elif user.lower() == 'tesoura':
    if pc.lower() == 'pedra':
        print('\033[31mDERROTA!\033[m')
    elif pc.lower() == 'papel':
        print('\033[32mVITÓRIA!\033[m')
    else:
        print('\033[33mEMPATE!\033[m')
else:
    print('Por favor, digite uma opção válida.')
