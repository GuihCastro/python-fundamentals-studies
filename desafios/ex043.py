# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

weight = float(input('Informe o seu peso (kg): '))
height = float(input('Informe a sua altura (m): '))
imc = weight / (height ** 2)

print('Seu IMC atual é {:.1f}.'.format(imc))

if imc < 18.5:
    print('Você está \033[31mABAIXO\033[m da sua faixa de peso ideal.')
elif 18.5 <= imc < 25:
    print('\033[1;32mParabéns\033[m! Você está \033[32mDENTRO\033[m da sua faixa de peso ideal.')
elif 25 <= imc < 30:
    print('Você está com \033[31mSOBREPESO\033[m.')
elif 30 <= imc < 40:
    print('Você está com \033[31mOBESIDADE\033[m.')
else:
    print('\033[1;31mCUIDADO\033[m! Você está com \033[31mOBESIDADE MÓRBIDA\033[m. É recomendado que procure um médico.')

