n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
rd = n1 % n2

print('A soma é {}\nA subtração é {}'.format(s, sub))
print('A multiplicação é {}\nA divisão é {:.2f}'.format(m, d), end=' | ')
print('A exponenciação, divisão inteira e resto da divisão são, respectivamente: {}, {} e {}'. format(e, di, rd))
