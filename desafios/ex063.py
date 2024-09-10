# Faça um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci
# Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8

print('=' * 50)
print('{:^50}'.format('SEQUÊNCIA DE FIBONACCI v1.O'))
print('=' * 50)

n = int(input('Informe quantos elementos da sequência você deseja ver: '))
c = 3
actual = 1
previous = 0
next = 0

print('{} → {}'.format(previous, actual), end=' → ')

while c <= n:
    next = actual + previous
    if c < n:
        print('{}'.format(next), end=' → ')
    else:
        print('{}'.format(next))
    previous = actual
    actual = next
    c += 1
