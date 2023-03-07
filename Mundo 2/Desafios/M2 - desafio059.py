# Mundo - Desafio 059
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep

flag_exit = False

valor_a = float(input("Digite o primeiro valor (A): "))
valor_b = float(input("Digite o segundo valor (B): "))

while not flag_exit:
    print("")
    print("MENU DE OPERAÇÕES")
    print('''[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa''')
    resposta_usuario = int(input(">>> Escolha uma das opções acima: "))
    print("")

    if resposta_usuario == 1:
        print("Operação - Soma")
        print("A soma entre os valores {:.2f} e {:.2f} é: {:.2f}".format(valor_a, valor_b, valor_a+valor_b))

    elif resposta_usuario == 2:
        print("Operação - Multiplicação")
        print("A multiplicação entre os valores {:.2f} e {:.2f} é: {:.2f}".format(valor_a, valor_b, valor_a * valor_b))

    elif resposta_usuario == 3:
        if valor_a > valor_b:
            print("O valor A - {:.2f} é maior que o valor B - {:.2f}".format(valor_a, valor_b))
        elif valor_b > valor_a:
            print("O valor B - {:.2f} é maior que o valor A - {:.2f}".format(valor_b, valor_a))
        else:
            print("A e B são iguais")

    elif resposta_usuario == 4:
        print("Operação - Inserir novos números")
        valor_a = float(input("Digite um novo valor de A: "))
        valor_b = float(input("Digite um novo valor de B: "))

    elif resposta_usuario == 5:
        flag_exit = True
        print("Saindo do programa... Volte sempre :)")
    else:
        print("Oops... Opção inválida! Digite uma das opções disponíveis.")

sleep(1)
