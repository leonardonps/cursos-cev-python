# Mundo - Desafio 068
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

qtd_vitorias = 0

print("JOGO ÍMPAR OU PAR")
print("PC: Bora jogar ímpar ou par?")

while True:
    opcao_jogador = ' '
    soma_par = False

    while opcao_jogador not in 'IP':
        opcao_jogador = str(input("Digite sua opção [I- ímpar ou P - par]: ")).upper().strip()[0]

    numero_jogador = int(input("Agora, digite um número: "))

    numero_computador = randint(0, 10)

    soma = numero_jogador + numero_computador

    print(f"A soma entre {numero_jogador} e {numero_computador} deu {soma}.")

    if soma % 2 == 0:
        soma_par = True

    if opcao_jogador == 'P':
        if soma_par:
            print("Parabéns! Você ganhou, a soma deu PAR.")
            qtd_vitorias += 1
        else:
            print("Não foi dessa vez. A soma deu ÍMPAR, logo o computador ganhou.")
            print("")
            break
    else:
        if soma_par:
            print("Não foi dessa vez. A soma deu PAR, logo o computador ganhou. ")
            print("")
            break
        else:
            print("Parabéns! Você ganhou, a soma deu ÍMPAR.")
            qtd_vitorias += 1

    print("=-" * 30)
    print("Vamos jogar novamente...")
    print("")

print(f"O jogou acabou... Veja quantas vezes você ganhou: {qtd_vitorias}")
