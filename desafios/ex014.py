# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

C = float(input('Informe a temperatura em graus celsius (ºC): '))
F = (C * 1.8) + 32

print('Essa temperatura corresponde a {:.1f}ºF (Farenheit)'.format(F))
