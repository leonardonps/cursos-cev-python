# Mundo 3 - Desafio 082
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores ímpares digitados,
# respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

values = []
even_values = []
odd_values = []

while True:
    value = int(input('Type a number, please: '))
    values.append(value)

    answer = str(input('Would you like type another number[Y/N]? ')).strip().upper()[0]
    if answer not in 'YN':
        answer = str(input('Ooops... You have typed an invalid option. Please, type Y for yes and N for no: ')).strip().upper()[0]
    if answer == 'N':
        break

for v in values:
    if v % 2 == 0:
        even_values.append(v)
    else:
        odd_values.append(v)

print(values)
print(even_values)
print(odd_values)