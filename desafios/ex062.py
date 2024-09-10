# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disse que quer mostrar 0 termos.

print('=' * 50)
print('{:^50}'.format('SUPER PROGRESSÃO ARITMÉTICA v3.O'))
print('=' * 50)

first = int(input('Informe o primeiro termo da PA: '))
reason = int(input('Informe a razão da PA: '))
n = first
terms = 10
c = 0

while terms > 0:
    if terms > 1:
        print(n, end=', ')
        terms -= 1
    else:
        print(n)
        terms = int(input('Você deseja mostrar mais termos?\nSe sim, informe o número desejado, se não, "0" para encerrar: '))
    n += reason
    c += 1

print('A progressão foi finalizada com {} termos sendo exibidos.'.format(c))
