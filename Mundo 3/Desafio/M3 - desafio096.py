# Mundo 3 - Desafio 096
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.

def area(width, length):
    area = width * length
    print(f'This land with width = {width:.2f}m and length {length:.2f}m has {area:.2f}m² of area.')


# Main program
width = float(input("Type the land's width: "))
length = float(input("Type the land's length: "))

area(width, length)