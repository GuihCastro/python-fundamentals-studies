# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar mais valores.

print('=' * 50)
print('{:^50}'.format('MÉDIA, MAIOR E MENOR VALORES'))
print('=' * 50)

proceed = 's'
greatest = smallest = 0
i = 0
s = 0

while proceed != 'n':
    n = int(input('Informe um número inteiro para ser computado: '))
    s += n
    if i == 0:
        greatest = n
        smallest = n
    else:
        if n > greatest:
            greatest = n
        if n < smallest:
            smallest = n
    i += 1
    proceed = str(input('Deseja continuar? [S/N]: ')).strip().lower()
    while proceed != 'n' and proceed != 's':
        proceed = str(input('Deseja continuar? [S/N]: ')).strip().lower()

average = s / i

print('Você informou um total de {} números.\nO maior deles foi: {}\nO menor foi: {}\nE a média entre todos foi: {:.1f}.'.format(i, greatest, smallest, average))
