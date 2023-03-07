# Mundo 2 - Desafio 045
# Crie um programa que faça o computador jogar Jokenpô com você

import random

print("JOGO - JOKENPÔ");
print("Bora brincar de Pedra, papel e tesoura?")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

op_user = int(input("Escolha uma das opções acima: "))

op_pc = random.randint(1,3)
print("Opção escolhida do PC: {}".format(op_pc))

print("=-" * 20)
if (op_user == 1 and op_pc == 3) or (op_user == 2 and op_pc == 1) or (op_user == 3 and op_pc == 2):

    if op_user == 1 and op_pc == 3:
        print("Você: Pedra   X   PC: Tesoura")

    if op_user == 2 and op_pc == 1:
        print("Você: Papel   X   PC: Pedra")

    if op_user == 3 and op_pc == 2:
        print("Você: Tesoura   X   PC: Papel")

    print("Parabéns! Você venceu :)")

elif (op_user == 1 and op_pc == 2) or (op_user == 2 and op_pc == 3) or (op_user == 3 and op_pc == 1):

    if op_user == 1 and op_pc == 2:
        print("Você: Pedra   X   PC: Papel")

    if op_user == 2 and op_pc == 3:
        print("Você: Papel   X   PC: Tesoura")

    if op_user == 3 and op_pc == 1:
        print("Você: Tesoura   X   PC: Pedra")

    print("Não foi dessa vez! Você perdeu. :(")

else:

    if op_user == 1 and op_pc == 1:
        print("Você: Pedra   X   PC: Pedra")

    if op_user == 2 and op_pc == 2:
        print("Você: Papel   X   PC: Papel")

    if op_user == 3 and op_pc == 3:
        print("Você: Tesoura   X   PC: Tesoura")

    print("Ihhh! Deu empate! Bora jogar mais uma vez?")

print("=-"*20)