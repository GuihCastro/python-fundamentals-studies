# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

print('=' * 50)
print(f'{'BOLETIM COM LISTAS COMPOSTAS':^50}')
print('=' * 50)

students = []

while True:
    student = []
    notes = []
    student.append(str(input('Nome: ')).strip())
    notes.append(float(input('Nota 1: ')))
    notes.append(float(input('Nota 2: ')))
    student.append(notes.copy())
    students.append(student.copy())
    student.clear()
    proceed = str(input('Deseja continuar? [S/N]: ')).strip().lower()
    while proceed != 's' and proceed != 'n':
        proceed = str(input('Por favor, informe uma opção válida.\nDeseja continuar? [S/N]: ')).strip().lower()
    if proceed == 'n':
        break

print('=-' * 25)

print(students)

print('No. Nome                Média')
print('-' * 30)
for i, s in enumerate(students):
    average = (s[1][0] + s[1][1]) / 2
    print(f'{i+1:<4}', end='')
    print(f'{s[0]:<20}', end='')
    print(f'{average:<5.1f}')
print('-' * 30)

while True:
    option = int(input('Mostrar notas de qual aluno ("999" interrompe)? '))
    while option != 999 and option > len(students):
        option = int(input('Por favor, informe uma opção válida.\nMostrar notas de qual aluno ("999" interrompe)? '))
    if option == 999:
        print('Finalizando...')
        break
    print(f'Notas de {students[option-1][0]}: {students[option-1][1]}')
    print('-' * 30)
