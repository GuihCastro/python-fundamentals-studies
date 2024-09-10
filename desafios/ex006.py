# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

number = int(input('Informe um número: '))
double = number * 2
triple = number * 3
square = number ** (1/2)

print('Dobro: {}\nTriplo: {}\nRaiz Quadrada: {:.2f}'.format(double,triple, square))
