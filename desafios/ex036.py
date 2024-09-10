# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('=' * 30)
print('\033[1;34mCALCULADORA DE FINANCIAMENTO\033[m')
print('=' * 30)

price = float(input('Informe o valor da casa: R$'))
salary = float(input('Agora, informe o seu salário: R$'))
years = int(input('Em quantos anos você pretende pagar? '))
installments = years * 12
installment_price = price / installments

print('Para comprar este imóvel em {} anos, você deverá pagar {} prestações de R${:.2f}.'.format(years, installments, installment_price))

if installment_price <= salary * 0.3:
    print('Você \033[1;32mPODE\033[m comprar esse imóvel nessas condições com o seu salário.')
else:
    print('Você \033[1;31mNÃO PODE\033[m comprar esse imóvel nessas condições com o seu salário.')
