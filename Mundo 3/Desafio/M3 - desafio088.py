# Mundo 3 - Desafio 088
# Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

bet = list()
bets = list()

number_bets = int(input('How many bets would you like to play? '))

for i in range(0, number_bets):
    for j in range(0, 6):
        number = randint(1,60)
        while number in bet:
            number = randint(1, 60)
        bet.append(number)
    bet.sort()
    bets.append(bet[:])
    bet.clear()

print("I've calculated the bets you wanted. Here are: ")
for c, b in enumerate(bets):
    print(f'Bet {c+1}: {b}')
    sleep(0.75)
