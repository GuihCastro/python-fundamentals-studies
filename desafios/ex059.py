# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
#
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

print('=' * 50)
print('{:^50}'.format('MENU DE OPERAÇÕES'))
print('=' * 50)

n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))

option = 0

while option != 5:
    option = int(input('''Escolha uma opção
    [\033[33m1\033[m] \033[34msomar\033[m
    [\033[33m2\033[m] \033[34mmultiplicar\033[m
    [\033[33m3\033[m] \033[34mmaior\033[m
    [\033[33m4\033[m] \033[34mnovos números\033[m
    [\033[33m5\033[m] \033[34msair do programa\033[m
    Sua opção: '''))

    if option == 1:
        print('A soma entre {} e {} é igual a: {}.'.format(n1, n2, n1+n2))
    elif option == 2:
        print('O produto da multiplicação entre {} e {} é: {}.'.format(n1, n2, n1*n2))
    elif option == 3:
        if n1 > n2:
            print('Entre {} e {} o maior número é: {}.'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {} o maior número é: {}.'.format(n1, n2, n2))
        else:
            print('{} e {} são iguais, portanto não há maior valor entre eles.'.format(n1, n2))
    elif option == 4:
        n1 = float(input('Informe um novo primeiro valor: '))
        n2 = float(input('Informe um novo segundo valor: '))
    elif option == 5:
        print('Finalizando...')
    else:
        print('Por favor, informe uma opção válida.')
    print('=-=' * 10)
    sleep(1)

print('FIM!')
