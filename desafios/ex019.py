# Um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice

# names = [
#    str(input('Informe o nome do primeiro aluno: ')),
#    str(input('Informe o nome do segundo aluno: ')),
#    str(input('Informe o nome do terceiro aluno: ')),
#    str(input('Informe o nome do quarto aluno: '))
#]
name_1 = str(input('Informe o nome do primeiro aluno: '))
name_2 = str(input('Informe o nome do segundo aluno: '))
name_3 = str(input('Informe o nome do terceiro aluno: '))
name_4 = str(input('Informe o nome do quarto aluno: '))
names = [name_1, name_2, name_3, name_4]
chosen_student = choice(names)

print('O(a) aluno(a) sorteado(a) foi: {}.'.format(chosen_student))
