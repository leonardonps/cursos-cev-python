# Mundo 3 - Desafio 113
# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de
# tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def readInt(msg):
    isInt = False
    while not isInt:
        try:
            number = int(input(msg))
        except (KeyboardInterrupt):
            print('\033[31mUser didn\'t prefer to type a number.\033[m')
            return 0
        except:
            print('\33[31mType a valid INTEGER number.\33[m')
        else:
            isInt = True
            return number


def readFloat(msg):
    isFloat = False
    while not isFloat:
        try:
            number = float(input(msg))
        except (KeyboardInterrupt):
            print('\033[31mUser didn\'t prefer to type a number.\033[m')
            return 0
        except:
            print('\33[31mType a valid FLOAT number.\33[m')
        else:
            isFloat = True
            return number



intNumber = readInt('Type a integer number: ')
floatNumber = readFloat('Type a float number: ')

print('The number that you typed was: ' + str(intNumber))
print('The number that you typed was: ' + str(floatNumber))
