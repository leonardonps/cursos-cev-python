# Mundo 1 - Desafio 016
# Crie um programa que leia um número Real qualquer
# pelo teclado e mostre na tela a sua porção inteira
# Exemplo:
# digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

from math import trunc

num = float(input('Digite um número: '))
print('O número {} tem como sua porção inteira igual a: {}.'.format(num, trunc(num)))

