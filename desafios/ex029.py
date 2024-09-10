# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassado 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

speed = float(input('Informe a velocidade do carro (em km/h): '))
fine = (speed - 80) * 7

if speed > 80:
    print('Você foi multado!')
    print('Deverá pagar R${:.2f} de multa.'.format(fine))
else:
    print('Você está dentro do limite. Boa viagem!')
