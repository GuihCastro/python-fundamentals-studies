# Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A".
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.

phrase = str(input('Digite uma frase: ')).strip()

print('A letra "a" aparece {} vezes nessa frase.'.format(phrase.lower().count('a')))
print('Ela aparece pela primeira vez na posição {} e pela última vez na posição {}.'.format(phrase.lower().find('a') + 1, phrase.lower().rfind('a') + 1))
