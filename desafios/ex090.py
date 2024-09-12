# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

print('=' * 50)
print(f'{'DICIONÁRIO EM PYTHON':^50}')
print('=' * 50)

student = dict()
status = 'Aprovado'
student['name'] = str(input('Nome: ')).strip()
student['average'] = float(input(f'Média de {student['name']}: '))
while student['average'] < 0 or student['average'] > 10:
    student['average'] = float(input(f'Por favor, informe uma nota válida (entre 0 e 10)\nMédia de {student["name"]}: '))
if student['average'] < 5:
    status = 'Reprovado'
elif student['average'] < 7:
    status = 'Recuperação'

print('-' * 30)

print(f'Nome do aluno: {student["name"]}')
print(f'Média do aluno: {student["average"]:.1f}')
print(f'Sua situação é: {status}')
