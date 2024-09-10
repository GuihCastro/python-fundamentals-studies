name = str(input('Qual é o seu nome? '))
if name.lower() == 'guilherme':
    print('Que nome bonito!')
elif name.lower() == 'pedro' or name.lower() == 'maria' or name.lower() == 'paulo':
    print('Seu nome é bem popular no Brasil.')
elif name.lower() in 'mariana cleide marta geralda':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normalzinho...')
print('Tenha um bom dia, {}!'.format(name))