# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('{:=^50}'.format(' TABUADA '))

n = int(input('Informe um número inteiro: '))

for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, (n * c)))
