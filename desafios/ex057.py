# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

print('=' * 50)
print('{:^50}'.format('VALIDAÇÃO DE DADOS'))
print('=' * 50)

gender = ''

while gender != 'm' and gender != 'f':
    gender = str(input('Informe o seu sexo [M/F]: ')).strip().lower()
    if gender != 'm' and gender != 'f':
        print('Por favor, informe um valor válido ("M" ou "F")')
    else:
        if gender == 'm':
            print('Obrigado! Seja bem-vindo!')
        else:
            print('Obrigado! Seja bem-vinda!')

print('FIM!')
