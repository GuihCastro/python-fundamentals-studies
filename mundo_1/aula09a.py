frase = 'Curso em Vídeo Python'

# fatiamento
print(frase[1:13:2])
# contagem
print(frase.count('o'))
# tamanho
print(len(frase))
# substituir
print(frase.replace('Python', 'Java'))
# verificação
print('Curso' in frase)
# encontrar
print(frase.lower().find('vídeo'))
# dividir
splited = frase.split()
print(splited)
# juntar
print('-'.join(splited))
