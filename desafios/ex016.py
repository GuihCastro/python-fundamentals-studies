# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
# Ex: Digite um número: 6.127 | O número 6.127 tem a parte inteira 6.

from math import trunc

num = float(input('Digite um número: '))
num_int = trunc(num)

print('O número {} tem a parte inteira {}.'.format(num, num_int))
