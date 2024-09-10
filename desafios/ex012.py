# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

price = float(input('Informe o preço do produto: R$'))
discount = price * 0.05
new_price = price - discount

print('O valor final, com 5% de desconto, será de R${:.2f}'. format(new_price))
