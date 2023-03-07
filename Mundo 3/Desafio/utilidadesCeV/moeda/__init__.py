def increase(value, percent, formatted=True):

    new_value = value + value*(percent/100)

    if formatted == True:
        return currency(new_value)

    return new_value


def decrease(value, percent, formatted=True):

    new_value = value - value*(percent/100)

    if formatted == True:
        return currency(new_value)

    return new_value


def half(value, formatted=True):
    new_value = value/2

    if formatted == True:
        return currency(new_value)

    return new_value


def double(value, formatted=True):
    new_value = value*2

    if formatted == True:
        return currency(new_value)

    return new_value


def currency(value, currency='RS$'):
    return currency + str(format(value, '.2f')).replace('.', ',')


def summary(value, increase_percent, decrease_percent):

    print('='*40)
    print('{:^40}'.format("Summary of the value")) #print('Summary of the value'.center(30))
    print('='*40)

    print(f"Analysed price: {currency(value):>21}")
    print(f"Double: {double(value):>29}")
    print(f"Half: {half(value):>31}")
    print(f"Increase of {increase_percent}%: {increase(value, increase_percent):>20}")
    print(f"Decrease of {decrease_percent}%: {decrease(value, decrease_percent):>20}")
    print('-'*40)

