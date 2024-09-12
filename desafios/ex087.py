# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

print('=' * 50)
print(f'{'MAIS SOBRE MATRIZ EM PYTHON':^50}')
print('=' * 50)

matrix = [[], [], []]
even = []
even_sum = third_column_sum = 0

for l in range(0, 3):
    for c in range(0, 3):
        n = (int(input(f'Digite um valor para [{l}, {c}]: ')))
        matrix[l].append(n)
        if n % 2 == 0:
            even.append(n)

for n in even:
    even_sum += n

third_column_sum += matrix[0][2] + matrix[1][2] + matrix[2][2]

print('-' * 50)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end=' ')
    print()

print('-' * 50)

print(f'A soma dos valores pares é: {even_sum}')
print(f'A soma dos valores da terceira coluna é: {third_column_sum}')
print(f'O maior valor da segunda linha é: {max(matrix[1])}')
