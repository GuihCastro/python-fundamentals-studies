# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

number = int(input('Informe um número inteiro: '))
t1 = number * 1
t2 = number * 2
t3 = number * 3
t4 = number * 4
t5 = number * 5
t6 = number * 6
t7 = number * 7
t8 = number * 8
t9 = number * 9
t10 = number * 10

print('-' * 15)
print('Tabuada de {0}:\n{0:2} x 1 = {1:2}\n{0:2} x 2 = {2:2}\n{0:2} x 3 = {3:2}\n{0:2} x 4 = {4:2}\n{0:2} x 5 = {5:2}\n{0:2} x 6 = {6:2}\n{0:2} x 7 = {7:2}\n{0:2} x 8 = {8:2}\n{0:2} x 9 = {9:2}\n{0:2} x 10 = {10:2}'.format(number, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10))
print('-' * 15)
