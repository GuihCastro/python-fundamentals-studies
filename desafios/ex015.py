# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.

km = float(input('Informe a quilometragem percorrida com o veículo: '))
days = int(input('Agora, informe a quantidade de dias pelos quais ele foi alugado: '))
price_km = km * 0.15
price_days = days * 60
price_total = price_km + price_days

print('O valor total a ser pago pelo aluguel é de R${:.2f}'.format(price_total))
