# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

grade_1 = float(input('Informe a primeira nota: '))
grade_2 = float(input('Informe a segunda nota: '))
average = (grade_1 + grade_2) / 2

print('A média é: {:.1f}'.format(average))
