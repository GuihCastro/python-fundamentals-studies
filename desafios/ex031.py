# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.

distance = float(input('Informe a distância da viagem (em km): '))
price = 0

if distance <= 200:
    price = distance * 0.5
else:
    price = distance * 0.45

print('O valor dessa viagem será de R${:.2f}.'.format(price))
