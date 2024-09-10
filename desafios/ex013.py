# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salary = float(input('Informe o salário do funcionário: R$'))
increase = salary * 0.15
new_salary = salary + increase

print('O novo salário, com um aumento de 15%, será de R${:.2f}'.format(new_salary))
