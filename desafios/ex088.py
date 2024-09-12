# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('=' * 50)
print(f'{'PALPITES PARA A MEGA SENA':^50}')
print('=' * 50)

games = int(input('Quantos jogos você deseja sortear? '))
games_list = []

print(f'{f' SORTEANDO {games} JOGOS ':-^50}')

for g in range(0, games):
    game = []
    while len(game) < 6:
        n = randint(1, 60)
        if n not in game:
            game.append(n)
    games_list.append(game.copy())
    game.clear()

sleep(.5)

for i, game in enumerate(games_list):
    print(f'Jogo {i+1}: {game} ')
    sleep(.5)

print(f'{' [ BOA SORTE! ] ':-^50}')
