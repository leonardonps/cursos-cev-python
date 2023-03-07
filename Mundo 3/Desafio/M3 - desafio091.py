# Mundo 3 - Desafio 091
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

players = {'Player 1': randint(1,6),
           'Player 2': randint(1,6),
           'Player 3': randint(1,6),
           'Player 4': randint(1,6)}

for k, v in players.items():
    print(f'{k}: {v}')

print('Order of the players based on crescending values: ')

for i in sorted(players, key = players.get, reverse=True):
    print(f'{i}: {players[i]}')

'''
Solução de Guanabara:

from random import randint
from time import sleep
from operator import itemgetter

jogo = { 'jogador1': randint(1,6)
         'jogador2': randint(1,6)
         'jogador3': randint(1,6)
         'jogador4': randint(1,6)}

ranking = list()

print('Valores sorteados:')

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
    
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print('=== RANKING DOS JOGADORES ===')

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

'''


