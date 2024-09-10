values = []

for count in range(0, 5):
    values.append(int(input('Digite um valor: ')))
    
for index, value in enumerate(values):
    print(f'Na posição {index} encontrei o valor {value}!')

print('Cheguei ao final da lista.')
