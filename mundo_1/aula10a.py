name = str(input('Qual é o seu nome? '))

if name.lower() == 'guilherme':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')

print('Bom dia, {}!'.format(name))
