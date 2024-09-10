# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

print('=' * 50)
print(f'{'ANÁLISE DE DADOS DO GRUPO':^50}')
print('=' * 50)

above_18 = men = women_under_20 = 0

while True:
    print('-' * 30)
    print(f'{'CADASTRE UMA PESSOA':^30}')
    print('-' * 30)
    age = int(input('Idade: '))
    gender = str(input('Sexo [M/F]: ')).strip().lower()
    while gender != 'm' and gender != 'f':
        print('Por favor, informe uma opção válida.')
        gender = str(input('Sexo [M/F]: ')).strip().lower()
    if age > 18:
        above_18 += 1
    if gender == 'm':
        men += 1
    if gender == 'f' and age < 20:
        women_under_20 += 1
    print('Cadastro realizado com sucesso!')
    print('-' * 30)
    proceed = str(input('Quer continuar? [S/N]: ')).strip().lower()
    while proceed != 's' and proceed != 'n':
        print('Por favor, informe uma opção válida.')
        proceed = str(input('Quer continuar? [S/N]: ')).strip().lower()
    print('-' * 30)
    if proceed == 'n':
        break

print(f'{' FIM DO CADASTRO ':=^30}')
print(f'Total de pessoas cadastradas com mais de 18 anos: {above_18}')
print(f'Total de homens cadastrados: {men}')
print(f'Total de mulheres cadastradas com menos de 20 anos: {women_under_20}')
