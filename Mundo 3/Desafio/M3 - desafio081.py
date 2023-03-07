# Mundo 3 - Desafio 081
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

values = []
counter = 0

while True:
    value = int(input('Type a number, please: '))
    values.append(value)
    counter += 1

    answer = str(input("Would you like type another number[Y/N]? ")).strip().upper()[0]
    while answer not in 'YN':
        answer = str(input('Sorry, but you have typed an option wrongly. Please, type Y for yes and N for no: ')).strip().upper()[0]
    if answer == 'N':
        break

print(f'Number of typed values: {counter}')
values.sort(reverse=True)
print(f'Descending list of values {values}')
if 5 in values:
    print('Number 5 was typed and is in the list.')