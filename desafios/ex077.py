# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

words = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for word in words:
    print(f'\nNa palavra {word.upper()} temos as vogais:', end=' ')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f'{letter}', end=' ')
