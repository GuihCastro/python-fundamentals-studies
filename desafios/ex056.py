# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# > A média de idade do grupo
# > Qual é o nome do homem mais velho.
# > Quantas mulheres têm menos de 20 anos.

from math import floor

ages_total = 0
ages_average = 0
older_man = ''
older_man_age = 0
women_under_20 = 0

for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    gender = str(input('Sexo (F/M): ')).strip().lower()

    ages_total += age

    if gender == 'm':
        if age > older_man_age:
            older_man_age = age
            older_man = name
    elif gender == 'f':
        if age < 20:
            women_under_20 += 1
    else:
        print('Foi informada uma opção inválida para o campo "sexo".')

ages_average = ages_total / 4

print('\nA média de idade do grupo é de {} anos.'.format(floor(ages_average)))
print('O homem mais velho se chama {} e tem {} anos.'.format(older_man, older_man_age) if older_man != '' else 'Não há homens no grupo.')
print('{} mulher(es) do grupo tem menos de 20 anos.'.format(women_under_20) if women_under_20 != 0 else 'Não há mulheres com menos de 20 anos no grupo.')
