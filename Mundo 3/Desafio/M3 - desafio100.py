# Mundo 3 - Desafio 100
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES
# sorteados pela função anterior.

# from random import sample
#
# numbers = list()
#
# def draw(numbers):
#     drawn_numbers = sample(numbers, 5)
#     return drawn_numbers
#
# def addEvens(drawn_numbers):
#     total = 0
#     print(drawn_numbers)
#     for el in drawn_numbers:
#         if el % 2 == 0:
#             total += el
#     print(total)
#
# # Main program
#
# while True:
#     number = int(input('Type a number: '))
#
#     numbers.append(number)
#
#     ans = str(input('Would you like to add another number [Y/N]? ')).strip().upper()[0]
#     while ans not in 'YN':
#         ans = str(input('Invalid option! Please, type Y for yes or N for no: ')).strip().upper()[0]
#     if ans == 'N':
#         break
#
# if len(numbers) >= 5:
#     drawn_numbers = draw(numbers)
#     addEvens(drawn_numbers)
# else:
#     print('ERROR! The list of numbers needs to have a length equals to 5 or over.')

from random import randint

numbers = list()

def drawNumbers():
    for _ in range(0, 5):
        number = randint(0, 10)
        while number in numbers:
            number = randint(0, 10)
        numbers.append(number)

def addEvens():
    sum = 0
    for el in numbers:
        if el % 2 == 0:
            sum += el
    print(sum)

drawNumbers()
print(numbers)
addEvens()