# Mundo 3 - Desafio 098
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a
# contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada (de menor ao maior; de maior ao menor; se passo negativo, transformá-lo em positivo; se
# == 0, passo tem que ser de 1 em 1)

from time import sleep

def counter(start, end, step):
    if step == 0:
        step = 1
    if start < end:
        step = abs(step)
        for c in range(start, end+1, step):
            print(f'{c} ', end='')
            sleep(0.25)
        print('END!')
    elif start > end:
        step = -abs(step)
        for c in range(start, end-1, step):
            print(f'{c} ', end='')
            sleep(0.25)
        print('END!')
    else:
        print('Start and End have same value. Try it with another values...')


# Main program

counter(1, 10, 0)
print('-=' * 20)
counter(10, 0, -2)
print('-=' * 20)

start = int(input("Now, let's personalizate the counter. Type a start: "))
end = int(input('Type an end: '))
step = int(input('Type the number of steps: '))
print('-' * 40)

counter(start, end, step)

