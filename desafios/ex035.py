# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('=' * 50)
print('Analisador de Triângulos')
print('=' * 50)

line_a = float(input('Informe o comprimento da primeira reta: '))
line_b = float(input('Informe o comprimento da segunda reta: '))
line_c = float(input('Informe o comprimento da terceira reta: '))

if ((line_a + line_b) > line_c) and ((line_a + line_c) > line_b) and ((line_c + line_b) > line_a):
    print('As retas informadas \033[32mPODEM\033[m formar um triângulo!')
else:
    print('As retas informadas \033[31mNÃO PODEM\033[m formar um triângulo!')
