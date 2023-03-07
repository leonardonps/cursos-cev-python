# Mundo 3 - Desafio 103
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos fols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def data(player='<unknown>', goals=0):
    """
    -> Simple function that receives two parameters, player's name and its goals
    :param player: this parameter receives the player's name, a string
    :param goals: this parameter receives total of goals scored by this player, a integer
    :return: no return
    """

    print(f'Player {player} scored {goals} goal(s).')

# Main program

name = str(input("Type player's name: "))
goals = input("Total of goals: ")

if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0

if name.strip() == '':
    data(goals=goals)
else:
    data(name, goals)