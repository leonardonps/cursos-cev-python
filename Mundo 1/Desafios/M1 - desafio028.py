# Mundo 1 - Desafio 028
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar desco
# brir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randrange
from time import sleep
#from randomi import randint

print("Bora fazer um desafio? Vou pensar em um número de 0 a 5 e você tenta adivinhar, pode ser?")
print("Tô pensando...")

num_pc = randrange(0,6)
# computador = randint(0,5)
#print(num_pc)

num_usuario = int(input("Pensei! Agora é a sua vez. Tente adivinhar um número escolhido: "))

print("PROCESSANDO...")
sleep(2)

if num_pc == num_usuario:
    print("É esse número mesmo! Parabéns, você acertou!")
else:
    print("Oops...Não foi dessa vez. O número é {}. Tente de novo.".format(num_pc))


