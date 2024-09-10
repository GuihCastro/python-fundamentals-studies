# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de cordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 30 anos: SÊNIOR
# - Acima: MASTER

from datetime import date

birth_year = int(input('Informe o ano de nascimento do(a) atleta (no formato "0000"): '))
actual_year = date.today().year
age = actual_year - birth_year

print('O(a) atleta tem {} anos.'.format(age))

if age <= 9:
    print('Categoria: \033[32mMIRIM\033[m.')
elif age <= 14:
    print('Categoria: \033[32mINFANTIL\033[m.')
elif age <= 19:
    print('Categoria: \033[32mJÚNIOR\033[m.')
elif age <= 25:
    print('Categoria: \033[32mSÊNIOR\033[m.')
else:
    print('Categoria: \033[32mMASTER\033[m.')
