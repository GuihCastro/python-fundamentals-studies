galera = list()
pessoa = list()
total_maior = total_menor = 0

for c in range(0, 3):
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Idade: ')))
    galera.append(pessoa.copy())
    pessoa.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor += 1

print(f'Temos {total_maior} maiores e {total_menor} menores de idade.')
