# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

print('\033[1;35m-\033[m' * 30)
print('\033[1;34mCONVERSOR DE BASE NUMÉRICA\033[m')
print('\033[1;35m-\033[m' * 30)

num = int(input('Informe um número inteiro qualquer: '))
option = int(input("""
Agora, informe uma das opções de conversão, digitando:
[\033[33m1\033[m] para binário
[\033[33m2\033[m] para octal
[\033[33m3\033[m] para hexadecimal
Sua opção: """))

if option == 1:
    print('{} convertido para binário é: {}'.format(num, bin(num)[2:]))
elif option == 2:
    print('{} convertido para octal é: {}'.format(num, oct(num)[2:]))
elif option == 3:
    print('{} convertido para hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('Por favor, informe uma opção válida.')
