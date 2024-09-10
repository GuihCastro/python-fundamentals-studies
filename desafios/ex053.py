# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

print('=' * 50)
print('{:^50}'.format(' IDENTIFICADOR DE PALÍNDROMOS '))
print('=' * 50)

phrase = str(input('Digite uma frase para saber se ela é um palíndromo (não use acentos): ')).strip().lower()
words = phrase.split()
to_analyze = ''.join(words)
reverse = ''.join(reversed(to_analyze))

print('A frase \033[34m{}\033[m \033[32mÉ\033[m um palíndromo!'.format(phrase) if to_analyze == reverse else 'A frase \033[34m{}\033[m \033[31mNÃO É\033[m um palíndromo.'.format(phrase))

print(to_analyze, reverse)
