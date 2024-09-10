# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando  número solicitado for negativo.

print('=' * 50)
print(f'{'TABUADA v3.0':^50}')
print('=' * 50)

while True:
    num = int(input('Informe um número para ver a sua Tabuada (ou digite um valor negativo para encerrar): '))
    print('-' * 10)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i:2} = {num * i}')
    print('-' * 10)

print('Programa encerrado!')
