# Mundo 2 - Desafio 046
# Faça um programa que mostra na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# uma pausa de 1 segundo entre eles.

from time import sleep

for c in range(10, -1, -1):
    print("{}...".format(c))
    sleep(1)
print("AGORA! POW POOOW POW POOOW")