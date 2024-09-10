# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

grade_1 = float(input('Informe a primeira nota: '))
grade_2 = float(input('Informe a segunda nota: '))
average = (grade_1 + grade_2) / 2

print('A média foi {:.1f}.'.format(average))

if average < 5.0:
    print('Aluno \033[1;31mREPROVADO!\033[m')
elif 5.0 <= average <= 6.9:
    print('Aluno em \033[1:33mRECUPERAÇÃO\033[m.')
else:
    print('Aluno \033[1;32mAPROVADO!\033[m')
