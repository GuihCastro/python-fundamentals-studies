# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

print('=' * 50)
print(f'{'MATRIZ EM PYTHON':^50}')
print('=' * 50)

matrix = [[], [], []]

for c in range(0, 3):
    matrix[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
    matrix[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
    matrix[2].append(int(input(f'Digite um valor para [2, {c}]: ')))

print('-' * 50)

print(f'''[ {matrix[0][0]} ] [ {matrix[0][1]} ] [ {matrix[0][2]} ]
[ {matrix[1][0]} ] [ {matrix[1][1]} ] [ {matrix[1][2]} ]
[ {matrix[2][0]} ] [ {matrix[2][1]} ] [ {matrix[2][2]} ]''')
