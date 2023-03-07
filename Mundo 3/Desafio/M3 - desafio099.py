# Mundo 3 - Desafio 099
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def highestValue(*list):
    for c, element in enumerate(list):
        if c == 0:
            highest_value = element
        elif element > highest_value:
            highest_value = element
    print(f'The highest value is: {highest_value}')


# Main program

highestValue(100, 2556, 3, 5, 8)