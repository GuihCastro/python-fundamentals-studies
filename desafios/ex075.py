# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

print('=' * 50)
print(f'{'ANÁLIDE DE DADOS EM TUPLA':^50}')
print('=' * 50)

values = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite um último número: ')))

print(f'Você digitou os valores: {values}')
if 9 in values:
    print(f'O valor 9 apareceu um total de {values.count(9)} vez(es).')
else:
    print('O valor 9 não foi digitado em nenhuma posição.')
if 3 in values:
    print(f'O valor 3 apareceu na {values.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram:', end=' ')
for n in values:
    if n % 2 == 0:
        print(n, end=' ')
