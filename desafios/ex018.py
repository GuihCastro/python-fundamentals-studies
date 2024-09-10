# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

rad = radians(float(input('Informe um ângulo: ')))
s = sin(rad)
c = cos(rad)
t = tan(rad)

print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(s, c, t))
