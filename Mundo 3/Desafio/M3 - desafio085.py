# Mundo 3 - Desafio 085
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
# os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


evens = list()
odds = list()
general = list()

for c in range (1, 8):
    value = int(input(f'[{c}] Type a number: '))
    if value % 2 == 0:
        evens.append(value)
    else:
        odds.append(value)

general.append(sorted(odds))
general.append(sorted(evens))

print(f'Even numbers: {general[0]}')
print(f'Odd numbers: {general[1]}')
