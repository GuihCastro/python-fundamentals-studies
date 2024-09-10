# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

print('=' * 50)
print(f'{'VALORES ÚNICOS EM UMA LISTA':^50}')
print('=' * 50)

values = []
while True:
    n = int(input('Digite um valor: '))
    if n not in values:
        values.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado. Não pode ser adicionado.')
    proceed = str(input('Quer continuar? [S/N]: ')).strip().lower()
    while proceed not in 'sn':
        proceed = str(input('Por favor, informe uma opção válida.\nQuer continuar? [S/N]: ')).strip().lower()
    if proceed == 'n':
        break
input('-=' * 25)
values.sort()
input(f'Você digitou os valores {values}')
