# Mundo 3 - Desafio 094
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) A média de idade do grupo
# c) Uma lista com todas as mulheres
# d) Uma lista com todas as pessoas com idade acima da média.

group = list()
person = dict()
total_ages = 0
women = list()
above_average = list()

while True:

    person['name'] = str(input("Type person's name: "))

    person['gender'] = str(input("Type person's gender [M/F]: ")).strip().upper()[0]
    while person.get('gender') not in 'MF':
        person['gender'] = str(input("Error! Please, type M for Male or F for Female: ")).strip().upper()[0]

    person['age'] = int(input("Type person's age: "))

    total_ages += person.get('age')
    if person.get('gender') == 'F':
        women.append(person.get('name'))

    group.append(person.copy())

    person.clear()

    ans = str(input('Would you like to add another person [Y/N]? ')).strip().upper()[0]
    while ans not in 'YN':
        ans = str(input('Please, type a valid option. Y for yes or N for No: ')).strip().upper()[0]
    if ans == 'N':
        break

average = total_ages/len(group)

for p in group:
    if p.get('age') > average:
        above_average.append(p.get('name'))

print(f'Number of people in the group: {len(group)}')
print(f'Average of age in the group: {average:.2f}')
print(f'Women list: {women}')
print(f'Above average age list: {above_average}')