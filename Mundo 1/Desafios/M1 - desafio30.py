# Mundo 1 - Desafio 030
# Crie um programa que leia um número inteiro e mostre na telas e ele é PAR ou ÍMPAR.

num = int(input("Digite um número: "))

if num % 2 == 0:
    print("O número: {} é PAR.".format(num))
else:
    print("O número: {} é ÍMPAR.".format(num))