# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# - À vista dinheiro / cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('{:=^50}'.format(' LOJAS H.C. '))

price = float(input('Valor da compra: R$'))
payment = int(input("""
Escolha a forma de pagamento (digitando o número correspondente)
[\033[33m1\033[m] - À vista no dinheiro ou cheque
[\033[33m2\033[m] - À vista no cartão
[\033[33m3\033[m] - Cartão - até 2x
[\033[33m4\033[m] - Cartão - 3x ou mais
Opção: """))

if payment == 1:
    total = price - (price * 0.1)
    print('\nO valor final, com 10% de \033[32mdesconto\033[m, será de R${:.2f}'.format(total))
elif payment == 2:
    total = price - (price * 0.05)
    print('\nO valor final, com 5% de \033[32mdesconto\033[m, será de R${:.2f}'.format(total))
elif payment == 3:
    installment_price = price / 2
    print('\nSua compra será paga em 2x, sem juros, de R${:.2f}\nO valor final permanece R${:.2f}'.format(installment_price, price))
elif payment == 4:
    total = price + (price * 0.2)
    installments = int(input('Informe o número de parcelas: '))
    installment_price = total / installments
    print('\nSua compra será para em {}x de R${:.2f}\nO valor final, com 20% de \033[31mjuros\033[m, será de R${:.2f}'.format(installments, installment_price, total))
else:
    print('\nPor favor, escolha uma opção válida.')
