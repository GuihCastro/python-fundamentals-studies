# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

print('=' * 50)
print(f'{'MAIOR E MENOR VALORES NA LISTA':^50}')
print('=' * 50)

values = [int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),
          int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')),
          int(input('Digite o quinto valor: '))]
greatest = max(values)
greates_positions = []
smallest = min(values)
smallest_positions = []

print('=-' * 25)

print('Você digitou os valores: ', end='')
for index, value in enumerate(values):
    print(value, end=' ')
    if value == greatest:
        greates_positions.append(index)
    if value == smallest:
        smallest_positions.append(index)
print(f'\nO maior valor digitado foi {greatest} na(s) posição(ões) {greates_positions}...')
print(f'O menor valor digitado foi {smallest} na(s) posição(ões) {smallest_positions}...')
