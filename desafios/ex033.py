# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
higher = 0
lower = 0

if n1 >= n2 and n1 >= n3:
    higher = n1
if n2 >= n1 and n2 >= n3:
    higher = n2
if n3 >= n1 and n3 >= n2:
    higher = n3

if n1 <= n2 and n1 <= n3:
    lower = n1
if n2 <= n1 and n2 <= n3:
    lower = n2
if n3 <= n1 and n3 <= n2:
    lower = n3

print('O MAIOR é {} e o MENOR é {}.'.format(higher, lower))
