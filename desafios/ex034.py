# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salary = float(input('Informe o salário do funcionário: R$'))
new_salary = 0

if salary > 1250:
    new_salary = salary + (salary * 0.1)
else:
    new_salary = salary + (salary * 0.15)

print('O novo salário será de R${:.2f}.'.format(new_salary))
