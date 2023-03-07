# Mundo 3 - Desafio 095
# Aprimore o Desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.

players = list()
player = dict()

while True:

    total_goals = 0

    player["name"] = str(input("Type player's name: "))
    player["games"] = int(input("Number of games: "))

    for c in range(1, player.get("games") + 1):
        goals = int(input(f'GAME {c} - Type the number of goals: '))
        player["Game " + str(c)] = goals
        total_goals += goals

    player['total_goals'] = total_goals

    players.append(player.copy())
    player.clear()

    ans = str(input('Would you like to add another player [Y/N]? ')).strip().upper()[0]
    while ans not in 'YN':
        ans = str(input('Please, type a valid option. Y for yes or N for No: ')).strip().upper()[0]
    if ans == 'N':
        break

print(players)
print('')
print('-='*20)

for c, p in enumerate(players):
    print(f'Identification number: {c}')
    p['id'] = c
    print(f'Name of the player: {p.get("name")}')
    print(f'Total of goals:  {p.get("total_goals")}')
    print('~-'*20)

ans = str(input('Would you like to see more details of a player [Y/N]? ')).strip().upper()[0]

while ans not in 'YN':
    ans = str(input('Please, type a valid option. Y - for yes or N - for No: ')).strip().upper()[0]

if ans == 'Y':
    player_id = int(input('Sure, type the identification number of the player who you want to see: '))
    print('')
    print('-='*20)
    for p in players:
        if player_id == p.get('id'):
            print(f'Name of the player: {p.get("name")}')
            print(f'Games which it played: {p.get("games")}')
            for c in range(1, p.get('games') + 1):
                print(f'Game {c}: {p.get("Game " + str(c))}')

            print(f'Total of goals of the player: {p.get("total_goals")}')


# Solução Guanabara
#
# time = list()
# jogador = dict()
# partidas = list()
#
# while True:
#
#     jogador.clear()
#     jogador['nome'] = str(input('Nome do jogador: '))
#     tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
#     partidas.clear()
#     for c in range(0, tot):
#         partidas.append(int(input(f'    Quantos gols na partida {c+1}?' )))
#     jogador['gols'] = partidas[:]
#     jogador['total'] = sum(partidas)
#     time.append(jogador.copy())
#     while True:
#         resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
#         if resp in 'SN':
#             break
#         print('Erro! Responda apenas S ou N: ').strip().upper()[0]
#         if resp == 'N':
#             break
#
# print('-=' * 30)
# print('cod ', end='')
# for i in jogador.keys():
#     print(f'{i:<15}', end='')
# print()
#
# print('-' * 40)
# for k, v in enumerate(time):
#     print(f'{k:>4} ', end='')
#     for d in v.values():
#         print(f'{str(d):<15}', end='')
#     print()
# print('-' * 40)
#
# while True:
#     busca = int(input('Mostrar dados de qual jogador? '))
#     if busca == 999:
#         break
#     if busca >= len(time):
#         print(f'Erro! Não existe jogador com código {busca}!')
#     else:
#         print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
#         for i, g in enumerate(time[busca]['gols']):
#             print(f'    No jogo {i+1} fez {g} gols.')
#     print('-' * 40)
# print(' <<< VOLTE SEMPRE >>>')