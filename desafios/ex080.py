# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

print('=' * 50)
print(f'{'LISTA ORDENADA SEM REPETIÇÕES':^50}')
print('=' * 50)

values = []

for count in range(0, 5):
    n = int(input('Digite um valor: '))
    if len(values) == 0:
        values.insert(0, n)
        print('Adicionado ao início da lista...')
    elif n < min(values):
        values.insert(0, n)
        print('Adicionado ao início da lista...')
    elif n > max(values):
        values.append(n)
        print('Adicionado ao final da lista...')
    else:
        for i, v in enumerate(values):
            if n < v:
                values.insert(i, n)
                print(f'Adicionado na posição {i}...')
                break
print(f'Os valores digitados, em ordem, foram: {values}')
