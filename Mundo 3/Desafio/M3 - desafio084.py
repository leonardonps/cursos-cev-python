# Mundo 3 - Desafio 084
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) Uma listagem com as pessoas mais pesadas
# c) Uma listagem com as pessoas mais leves

person = list()
group = list()
weightiest_group = list()
weightness_group = list()

while True:

    name = str(input('Type your name, please: '))
    weight = float(input('Now type your weight: '))

    person.append(name)
    person.append(weight)

    group.append(person[:])

    if len(group) == 1:
        weightiest = weightness = person[1]
    else:
        if person[1] > weightiest:
            weightiest = person[1]
        if person[1] < weightness:
            weightness = person[1]

    person.clear()

    ans = str(input('Would you like to add another person [Y/N]? ')).strip().upper()[0]
    while ans not in 'YN':
        ans = str(input("Sorry, but it isn't a valid option. Please, type Y for yes or N for no: ")).strip().upper()[0]
    if ans == 'N':
        break

for p in group:
    if p[1] == weightiest:
        weightiest_group.append(p[0])
    if p[1] == weightness:
        weightness_group.append(p[0])

print(f'People counter: {len(group)}')
print(f'The weightiest was {weightiest:.2f}kg.', end=" ")
for c, el in enumerate(weightiest_group):
    if c == len(weightiest_group) - 1:
        print(el, end=" ")
    elif c == len(weightiest_group) - 2:
        print(el, end=" and ")
    else:
        print(el, end=", ")
print('weigh it.')

print(f'The weightness was {weightness:.2f}kg.', end=" ")
for c, el in enumerate(weightness_group):
    if c == len(weightness_group) - 1:
        print(el, end=" ")
    elif c == len(weightness_group) - 2:
        print(el, end=" and ")
    else:
        print(el, end=", ")
print('weigh it.')
