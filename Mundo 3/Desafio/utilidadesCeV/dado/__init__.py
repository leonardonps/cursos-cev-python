def readCurrency(sentence):
    isValid = False
    while not isValid:
        value = str(input(sentence)).replace(',', '.').strip()
        if value.isalpha() or value.strip() == '':
            print(f'\033[31mError: \"{value}\" is not a valid price!\033[m')
        else:
            isValid = True
            return float(value)

def readInt(msg):
    isInt = False
    while not isInt:
        try:
            number = int(input(msg))
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
        except:
            print('\33[31mType a valid FLOAT number.\33[m')
        else:
            isFloat = True
            return number
