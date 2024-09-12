# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

print('=' * 50)
print(f'{'LISTA COM PARES E ÍMPARES':^50}')
print('=' * 50)

values = [[], []]

for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        values[0].append(n)
    else:
        values[1].append(n)

values[0].sort()
values[1].sort()

print('-' * 50)

print(f'Os valores pares digitados foram: {values[0]}')
print(f'Os valores ímpares digitados foram: {values[1]}')
