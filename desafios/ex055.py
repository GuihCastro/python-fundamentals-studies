# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

bigger = 0
smaller = 0

for p in range(1, 6):
    weight = float(input('Informe o {}º peso (kg): '.format(p)))
    if p == 1:
        bigger = weight
        smaller = weight
    else:
        if weight > bigger:
            bigger = weight
        if weight < smaller:
            smaller = weight

print('O maior peso lido foi {:.1f}kg, e o menor foi {:.1f}kg.'.format(bigger,smaller))
