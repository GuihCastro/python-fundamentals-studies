# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

print('=' * 50)
print(f'{'DIVIDINDO VALORES EM VÁRIAS LISTAS':^50}')
print('=' * 50)

values = []
even = []
odd = []
while True:
    n = int(input('Digite um número: '))
    values.append(n)
    proceed = str(input('Deseja continuar? [S/N]: ')).strip().lower()
    while proceed not in 'sn':
        proceed = str(input('Por favor, informe uma opção válida\nDeseja continuar? [S/N]: ')).strip().lower()
    if proceed == 'n':
        break
for v in values:
    if v % 2 == 0:
        even.append(v)
    else:
        odd.append(v)
print('-=' * 25)
print(f'A lista completa é: {values}')
print(f'A lista de pares é: {even}')
print(f'A lista de ímpares é: {odd}')
