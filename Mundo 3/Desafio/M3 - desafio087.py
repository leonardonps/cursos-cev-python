# Mundo 3 - Desafio 087
# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos os valores pares digitados
# b) A soma dos valores da terceira coluna
# c) O maior valor da segunda linha

row = list()
matrix = list()
even_sum = 0
third_col_sum = 0

for j in range(0, 3):
    for i in range(0, 3):
        value = int(input(f'[{j}][{i}] Type a number: '))
        row.append(value)
    matrix.append(row[:])
    row.clear()

print("-="*20)
print('{:^40}'.format('Matriz'))
for row in matrix:
    for c, element in enumerate(row):
        print(f'    [{element:^5}] ', end='')
        if element % 2 == 0:
            even_sum += element
        if c == 2:
            third_col_sum += element
    print('')

for element in matrix[1]:
    if element == matrix[1][0]:
        highest_value = element
    elif element > highest_value:
        highest_value = element

print('-='*20)
print(f'Even sum: {even_sum}')
print(f'Third column sum: {third_col_sum}')
print(f'Highest value in second row: {highest_value}')