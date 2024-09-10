# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

print('=' * 50)
print(f'{'MAIOR E MENOR VALORES EM TUPLA':^50}')
print('=' * 50)

from random import randint

n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)
numbers = (n1, n2, n3, n4, n5)
greatest = smallest = n1
print(f'Os valores sorteados foram:', end=' ')
for n in numbers:
    if n < smallest:
        smallest = n
    if n > greatest:
        greatest = n
    print(n, end=' ')
print(f'\nO maior valor sorteado foi {greatest}\nO menor valor sorteado foi {smallest}')
