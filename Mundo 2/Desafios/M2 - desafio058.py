# Mundo - Desafio 058
# Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print("=-*"*5, end=" ")
print("Jogo - Adivinhe em qual número estou pensando", end=" ")
print("=*"*5)
print("PC: Vou pensar em um número de 0 a 10. Chute qual será esse número e você ganha ;)")

numero_computador = randint(0, 10)
numero_tentativas = 0
acertou = False

while not acertou:
    numero_jogador = int(input("Jogador: "))
    numero_tentativas += 1

    if numero_computador == numero_jogador:
        acertou = True
    else:
        print("Oops... Não foi esse número que pensei. Tente outro :(")
        if numero_computador > numero_jogador:
            print("Chute mais pra cima...")
        else:
            print("Chute mais pra baixo...")

print("Parabéns, você ganhou! O número {} foi realmente o que pensei.".format(numero_computador))
print("Quantidade de tentativas: {}".format(numero_tentativas))
