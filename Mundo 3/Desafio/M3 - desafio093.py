# Mundo 3 - Desafio 093
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardade em um
# dicionário, incluindo o total de gols feitos durante o campeonato.
data_player = dict()
data_player["Name of the player"] = str(input("Type player's name: "))
data_player["Number of games"] = int(input("Number of games: "))

goals_total = 0

for c in range(1, data_player.get("Number of games")+1):
    goals = int(input(f'GAME {c} - Type the number of goals: '))
    data_player["Game " + str(c)] = goals
    goals_total += goals

print('')
print('-='*20)
for k, v in data_player.items():
    print(f'{k}: {v}')

print(f'Number of total goals: {goals_total}')

# Solução Guanabara
#
# jogador = dict()
# partidas = list()
#
# jogador['nome'] = str(input('Nome do jogador: '))
# tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
# for c in range(0, tot):
#     partidas.append(int(input(f'    Quantos gols na partida {c}?' )))
# jogador['gols'] = partidas[:]
# jogador['total'] = sum(partidas)
# print('-=' * 30)
# print(jogador)
# print('-=' * 30)
# for k, v in jogador.items():
#     print(f'O campo {k} tem o valor {v}')
# print('-=' * 30)
# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
# for i, v in enumerate(jogador['gols']):
#     print(f'    => Na partida {i} fez {v} gols.')
# print(f'Foi um total de {jogador["total"]} gols.')
