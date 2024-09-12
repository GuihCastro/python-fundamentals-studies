# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

print('=' * 50)
print(f'{'LISTA COMPOSTA E ANÁLISE DE DADOS':^50}')
print('=' * 50)

people = []
heavier_list = []
lighter_list = []
heavier_weight = lighter_weight = 0

while True:
    person = [
        str(input('Nome: ')).strip(),
        float(input('Peso: '))
    ]
    people.append(person.copy())
    print('Cadastrado com sucesso!')
    person.clear()
    proceed = str(input('Quer continuar? [S/N]: ')).strip().lower()
    while proceed != 's' and proceed != 'n':
        proceed = str(input('Por favor, informe uma opção válida.\nQuer continuar? [S/N]: '))
    if proceed == 'n':
        break

for i, p in enumerate(people):
    if i == 0:
        heavier_weight = p[1]
        lighter_weight = p[1]
        heavier_list.append(p[0])
        lighter_list.append(p[0])
    else:
        if p[1] == heavier_weight:
            heavier_list.append(p[0])
        elif p[1] > heavier_weight:
            heavier_weight = p[1]
            heavier_list.clear()
            heavier_list.append(p[0])
        if p[1] == lighter_weight:
            lighter_list.append(p[0])
        elif p[1] < lighter_weight:
            lighter_weight = p[1]
            lighter_list.clear()
            lighter_list.append(p[0])

print('-' * 50)
print(f'Foram cadastradas {len(people)} pessoas.')
print(f'O maior peso foi de {heavier_weight:.1f}kg. É o peso de: {heavier_list}')
print(f'O menor peso foi de {lighter_weight:.1f}kg. É o peso de: {lighter_list}')
