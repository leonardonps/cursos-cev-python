LINE_SIZE = 40


def header(sentence):
    line()
    print(sentence.center(40))
    line()


def line():
    print('-'*LINE_SIZE)


def menu(options_list):
    c = 1
    for op in options_list:
        print(f'{c} - {op}')
        c += 1

