# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('=' * 50)
print(f'{'LISTA DE PREÇOS COM TUPLA':^50}')
print('=' * 50)

products = ('Pão', 1, 'Leite', 4.99, 'Frango', 10.90)

for p in range(0, len(products), 2):
    print(f'{products[p]:.<42}', end='')
    print(f'R${products[p+1]:6.2f}')

print('-' * 50)
