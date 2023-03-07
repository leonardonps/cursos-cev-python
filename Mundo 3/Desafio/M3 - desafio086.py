# Mundo 3 - Desafio 086
# Crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matrix = list()
row = list()

for j in range(0, 3):
    for i in range(0, 3):
        value = int(input(f'[{j}][{i}] Type a number, please: '))
        row.append(value)
    matrix.append(row[:])
    row.clear()

print('-='*20)
print('{:^40}'.format('Matriz'))

for row in matrix:
    for element in row:
        print(f'    [{element:^5}] ', end='')
    print('')

