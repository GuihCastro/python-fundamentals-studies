from math import sqrt, floor

num = int(input('Digite um número: '))
root = sqrt(num)

print('A raiz quadrada de {} é igual a {:.2f}'.format(num, floor(root)))
