# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas.
# > O nome com todas minúsculas.
# > Quantas letras ao todo (sem considerar espaços).
# > Quantas letras tem o primeiro nome.

name = str(input('Digite seu nome completo: ')).strip()
uppercased = name.upper()
lowercased = name.lower()
splited = name.split()
no_space = ''.join(splited)
letter_quantity = len(no_space)
first_name_letter_quantity = len(splited[0])

print('O nome com todas as letras maiúsculas: {}\nCom todas minúsculas: {}\nQuantidade de letras ao todo (sem considerar espaços): {}\nQuantidade de letras do primeiro nome: {}'.format(uppercased, lowercased, letter_quantity, first_name_letter_quantity))
