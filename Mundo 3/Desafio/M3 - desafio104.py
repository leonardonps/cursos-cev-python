# Mundo 3 - Desafio 105
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que
# fazendo a validação para aceitar apenas um valor numérico.
# Ex.: n = leiaInt('Digite um n')

# About colors: https://www.geeksforgeeks.org/print-colors-python-terminal/ or https://en.wikipedia.org/wiki/ANSI_escape_code#Colors

def readInt(sentence):
    """
    Function determinates if an input is or not numeric
    :param sentence: this parameter receives a string that will be the input's message for user
    :return: no return
    """
    number = input(sentence)
    while not number.isnumeric():
        print("\033[31mWhat you typed isn't a numeric. \033[00m")
        number = input(sentence)

    return number


# Main program
number = readInt('Type a number: ')
print(f'The number that you typed was: {number}')
