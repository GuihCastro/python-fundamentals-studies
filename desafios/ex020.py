# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

name_1 = str(input('Informe o nome do primeiro aluno: '))
name_2 = str(input('Informe o nome do segundo aluno: '))
name_3 = str(input('Informe o nome do terceiro aluno: '))
name_4 = str(input('Informe o nome do quarto aluno: '))
names = [name_1, name_2, name_3, name_4]
shuffle(names)

print('A ordem de apresentação será:\n{}'.format(names))
