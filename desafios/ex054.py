# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

print('=' * 50)
print('{:^50}'.format(' ANALISADOR DE MAIORIDADE '))
print('=' * 50)

from datetime import date

actual_year = date.today().year
of_age = 0
minor = 0

for person in range(1, 8):
    birth_year = int(input('Informe o {}º ano de nascimento (no formato "0000"): '.format(person)))
    if actual_year - birth_year >= 18:
        of_age += 1
    elif actual_year - birth_year < 18:
        minor += 1

print('\nDas pessoas cujos anos de nascimento foram informadas, {} ainda \033[31mnão\033[m atingiram a maioridade, e {} já são \033[32mmaiores\033[m.'.format(minor, of_age))
