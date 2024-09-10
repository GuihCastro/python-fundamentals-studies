# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total de gasto na compra.
# B) Quantos produtos custam mais de R$1000,00.
# C) Qual é o nome do produto mais barato.

print('=' * 50)
print(f'{'ESTATÍSTICAS EM PRODUTOS':^50}')
print('=' * 50)

total = above_1000 = cheaper_price = 0
cheaper = ''

while True:
    name = str(input('Nome do produto: ')).strip()
    price = float(input('Preço: R$'))
    proceed = str(input('Quer continuar? [S/N]: ')).strip().lower()
    while proceed != 's' and proceed != 'n':
        print('Por favor, informe uma opção válida.')
        proceed = str(input('Quer continuar? [S/N]: ')).strip().lower()
    if total == 0 or price < cheaper_price:
        cheaper = name
        cheaper_price = price
    total += price
    if price > 1000:
        above_1000 += 1
    if proceed == 'n':
        break

print(f'{' Fim do programa! ':-^50}')
print(f'O total da compra foi: R${total:.2f}\nTemos {above_1000} produtos custando mais de R$1000,00\nO produto mais barato foi {cheaper}, que custa R${cheaper_price:.2f}')
