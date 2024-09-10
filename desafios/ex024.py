# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

city = str(input('Digite o nome de uma cidade: ')).strip()
starts_with_word = city.split()[0].lower() == 'santo'

print('O nome dessa cidade começa com a palavra "Santo"? {}'.format(starts_with_word))
