# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere US$1,00 = R$3,27

brl = float(input('Informe quanto você tem de dinheiro (em reais): R$'))
usd = brl / 5.50
eur = brl / 6.13
ars = brl / 0.0058

print('Com esse valor você pode comprar:\nUSD(dólar americano): ${:.2f}\nEUR(euro): ${:.2f}\nARS(peso argentino): ${:.2f}'.format(usd, eur, ars))
