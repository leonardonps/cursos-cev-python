# Mundo - Desafio 067
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input("Digite um número para saber sua tabuada [Para encerrar, digite um número negativo]: "))

    if numero < 0:
        break

    for i in range (0, 11):
        print(f"{numero} x {i} = {numero*i}")

    print('')