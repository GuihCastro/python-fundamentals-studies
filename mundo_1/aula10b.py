n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
average = (n1 + n2) / 2

print('A sua média foi: {:.1f}.'.format(average))

'''
if average >= 6.0:
    print('Foi uma boa média. PARABÉNS!')
else:
    print('Foi uma média ruim. ESTUDE MAIS!')
'''

print('Foi uma boa média. PARABÉNS!' if average >= 6.0 else 'Foi uma média ruim. ESTUDE MAIS!')
