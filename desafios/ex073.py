# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Corinthians.
from operator import index

print('=' * 50)
print(f'{'TUPLA COM TIMES DE FUTEBOL':^50}')
print('=' * 50)

table = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'São Paulo', 'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Internacional', 'Bragantino', 'Athletico-PR', 'Criciúma', 'Juventude', 'Grêmio', 'Fluminense', 'Corinthians', 'EC Vitória', 'Cuiabá', 'Atlético-GO')

print(f'Lista de times do Brasileirão {table}')
print('-=' * 50)
print(f'Os 5 primeiros são: {table[:5]}')
print('-=' * 50)
print(f'Os 4 últimos são: {table[-4:]}')
print('-=' * 50)
print(f'Times em órdem alfabética: {sorted(table)}')
print('-=' * 50)
print(f'O Corinthians está na {table.index('Corinthians')+1}ª posição')
