# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

print('=' * 50)
print(f'{'EXTRAINDO DADOS DE UMA LISTA':^50}')
print('=' * 50)

values = []

while True:
    values.append(int(input('Digite um valor: ')))
    print('Adicionado com sucesso...')
    proceed = str(input('Quer continuar? [S/N]: ')).strip().lower()
    while proceed not in 'sn':
        proceed = str(input('Por favor, informe uma opção válida.\nQuer continuar? [S/N]: ')).strip().lower()
    if proceed == 'n':
        break

values.sort(reverse=True)

print('-=' * 25)
print(f'Você digitou {len(values)} elementos.')
print(f'Os valores em ordem decrescente são: {values}')
print('O valor 5 \033[32mFAZ PARTE\033[m da lista!' if 5 in values else 'O valor 5 \033[31mNÃO FAZ PARTE\033[m da lista!')
