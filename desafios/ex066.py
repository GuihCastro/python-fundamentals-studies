# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

print('=' * 50)
print(f'{'VÁRIOS NÚMEROS COM FLAG':^50}')
print('=' * 50)

s = quantity = 0

while True:
    num = int(input('Informe um número inteiro (ou "999" para interromper): '))
    if num == 999:
        break
    s += num
    quantity += 1

print(f'A soma dos {quantity} números informados é: {s}')
