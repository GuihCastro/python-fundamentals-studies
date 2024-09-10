# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome, separadamente.
# Ex: Ana Maria de Souza | primeiro = Ana, último = Souza

name = str(input('Digite um nome completo: ')).strip()
name_splited = name.split()
first_name = name_splited[0]
last_name = name_splited[(len(name_splited) - 1)]

print('Primeiro nome: {}\nÚltimo nome: {}'.format(first_name.title(), last_name.title()))
