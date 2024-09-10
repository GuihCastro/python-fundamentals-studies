# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

print('\033[1;35m-\033[m' * 30)
print('\033[1;34mVERIFICADOR DE MAIOR NÚMERO INTEIRO\033[m')
print('\033[1;35m-\033[m' * 30)

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

if n1 > n2:
    print('\033[32m{}\033[m é maior do que \033[31m{}\033[m, portanto, o \033[1;33mprimeiro\033[m valor é o maior.'.format(n1, n2))
elif n1 < n2:
    print('\033[32m{}\033[m é maior do que \033[31m{}\033[m, portanto, o \033[1;33msegundo\033[m valor é o maior.'.format(n2, n1))
else:
    print('\033[33m{}\033[m e \033[33m{}\033[m são iguais, portanto, \033[31mnão existe\033[m maior valor.'.format(n1, n2))
