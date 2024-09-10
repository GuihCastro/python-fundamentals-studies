# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

gender = str(input('Informe o seu sexo (digitando "M" para Masculino e "F" para Feminino): '))

if gender.lower() == 'm':
    birth_year = int(input('Informe o ano em que você nasceu (no formato "0000"): '))
    actual_year = date.today().year
    age = actual_year - birth_year

    if age < 18:
        print('Você ainda vai se alistar ao serviço militar.\nRestam {} anos para o seu alistamento.'.format(18 - age))
        print('Seu alistamento será em {}.'.format(actual_year + (18 - age)))
    elif age == 18:
        print('Está na hora de você se alistar no serviço militar!')
    else:
        print('Você já passou da hora de se alistar no serviço militar.\nEstá {} anos atrasado.'.format(age - 18))
        print('Seu alistamento foi em {}.'.format(actual_year - (age - 18)))
elif gender.lower() == 'f':
    print('O alistameno não é obrigatório para você.')
else:
    print('Por favor, informe uma opção válida.')
