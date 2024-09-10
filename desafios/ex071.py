# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 50)
print(f'{'SIMULADOR DE CAIXA ELETRÔNICO':^50}')
print('=' * 50)

withdraw = int(input('Qual valor você quer sacar? R$'))
ballot_50 = ballot_20 = ballot_10 = ballot_1 = 0

while withdraw >= 50:
    withdraw -= 50
    ballot_50 += 1

while withdraw >= 20:
    withdraw -= 20
    ballot_20 += 1

while withdraw >= 10:
    withdraw -= 10
    ballot_10 += 1

while withdraw >= 1:
    withdraw -= 1
    ballot_1 += 1

print('Serão entregues:')
if ballot_50:
    print(f'{ballot_50} cédula(s) de R$50')
if ballot_20:
    print(f'{ballot_20} cédula(s) de R$20')
if ballot_10:
    print(f'{ballot_10} cédula(s) de R$10')
if ballot_1:
    print(f'{ballot_1} cédula(s) de R$1')
print('=' * 50)
print('Tenha um bom dia e volte sempre!')
