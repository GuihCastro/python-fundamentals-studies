# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

print('=' * 50)
print(f'{'MATRIZ EM PYTHON':^50}')
print('=' * 50)

matrix = [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        matrix[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

print('-' * 50)

print(f'''[{matrix[0][0]:^6}] [{matrix[0][1]:^6}] [{matrix[0][2]:^6}]
[{matrix[1][0]:^6}] [{matrix[1][1]:^6}] [{matrix[1][2]:^6}]
[{matrix[2][0]:^6}] [{matrix[2][1]:^6}] [{matrix[2][2]:^6}]''')
