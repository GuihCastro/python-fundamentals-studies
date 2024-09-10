# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print('=' * 50)
print('Analisador de Triângulos')
print('=' * 50)

line_a = float(input('Informe o comprimento da primeira reta: '))
line_b = float(input('Informe o comprimento da segunda reta: '))
line_c = float(input('Informe o comprimento da terceira reta: '))

if ((line_a + line_b) > line_c) and ((line_a + line_c) > line_b) and ((line_c + line_b) > line_a):
    print('As retas informadas \033[32mPODEM\033[m formar um triângulo!')
    if line_a == line_b == line_c:
        print('Será um triângulo \033[34mEquilátero\033[m.')
    elif line_a == line_b or line_a == line_c or line_b == line_c:
        print('Será um triângulo \033[34mIsósceles\033[m.')
    else:
        print('Será um triângulo \033[34mEscaleno\033[m.')
else:
    print('As retas informadas \033[31mNÃO PODEM\033[m formar um triângulo!')
