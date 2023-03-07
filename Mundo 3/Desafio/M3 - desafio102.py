# Mundo 3 - Desafio 101
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
# e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo
# do fatorial.

def factorial(number, show=False):
    """
    -> Function that calculates the factorial of a number.
    :param number: it receives the number which we want to know its factorial
    :param show: (optional) it is to define if we want to show all the calculation process or not
    :return: factorial of the received number.
    """
    base = 1
    for c in range(number, 0, -1):
        if show == True:

            print(f'{c}', end=' ')

            if c == 1:
                print('=', end=' ')
            else:
                print('*', end=' ')
        base *= c
    return base

# Main program
print(factorial(5, True))