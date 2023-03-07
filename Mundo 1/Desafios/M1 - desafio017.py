# Mundo 1 - Desafio 017
# Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triângulo,
# retângulo, calcule e mostre o comprimento da
# hipotenusa.
from math import pow, sqrt

co = float(input('Digite o cateto oposto do triângulo retângulo: '))
ca = float(input('Agora, digite o adjacente: '))
hip = sqrt(pow(co, 2) + pow(ca, 2))
#hip = math.hypot(co,ca)
print('O comprimento da hipotenusa é igual a: {:.2f}.'.format(hip))

