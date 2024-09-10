# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = str(input('Digite seu nome: ')).strip()
has_word = 'silva' in name.lower()

print('Você tem "Silva" no nome? {}'.format(has_word))
