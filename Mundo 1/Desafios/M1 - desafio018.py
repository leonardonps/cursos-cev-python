# Mundo 1 - Desafio 018
# Faça um programa que leia um ângulo qualquer e mostre
# na tela o valor do seno, cosseno e tangente desse ângulo.
import math

ang = float(input('Digite um valor do angulo em grau(º): '))
angRad = math.radians(ang)
angSin = math.sin(angRad)
angCos = math.cos(angRad)
angTan = math.tan(angRad)

print('O ângulo de {} tem o SENO de {:.2f}.'.format(ang, angSin))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(ang, angCos))
print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(ang, angTan))
