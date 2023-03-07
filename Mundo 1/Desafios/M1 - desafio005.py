# Mundo 1 - Desafio 005
# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor

num = int(input("Digite um número: "))
#print("Numero {} - seu antecessor é {} e seu sucessor é {}.".format(num, (num-1), (num+1)))
ant = num - 1
prox = num + 1
print("Numero {} - seu antecessor é {} e seu sucessor é {}.".format(num, ant, prox))