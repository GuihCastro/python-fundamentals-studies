# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('=' * 50)
print(f'{'JOGO DO PAR OU ÍMPAR':^50}')
print('=' * 50)

wins = 0

while True:
    pc = randint(0, 10)
    player_value = int(input('Diga um valor: '))
    player_option = str(input('Par ou Ímpar? [P/I]: ')).strip().lower()
    result = pc + player_value

    print(f'Você jogou {player_value} e o computador, {pc}. Total de {result}')
    print('-' * 20)

    if player_option == 'p':
        if result % 2 == 0:
            wins += 1
            print('Deu PAR!\nVocê VENCEU!\nVamos jogar novamente...')
            print('-' * 20)
        else:
            print('Deu ÍMPAR!\nVocê PERDEU!')
            break
    elif player_option == 'i':
        if result % 2 != 0:
            wins += 1
            print('Deu ÍMPAR!\nVocê VENCEU!\nVamos jogar novamente...')
            print('-' * 20)
        else:
            print('Deu PAR!\nVocê PERDEU!')
            break
    else:
        print('Por favor, informe uma opção válida...')

print('=' * 30)
print(f'GAME OVER! Total de vitórias: {wins}')
