# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostra o comprimento da hipotenusa

from math import pow, sqrt, hypot

cateto_oposto = float(input('Informe o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))
hipotenusa = sqrt((pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)))
hipot = hypot(cateto_oposto, cateto_adjacente)

print('O valor da hipotenusa é {:.1f}.'.format(hipot))
