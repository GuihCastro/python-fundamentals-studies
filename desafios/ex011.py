# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

height = float(input('Informe a altura da parede (em metros): '))
width = float(input('Informe a largura (também em metros): '))
area = height * width
ink = area / 2

print('Essa parede tem uma área de {:.2f}m², portanto você precisará de {:.2f} litros de tinta para pintá-la.'.format(area, ink))
