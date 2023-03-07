# Mundo 3 - Desafio 040
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta
# de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

values = []

for c in range(0,5):
    value_currently = int(input(f'[{c}] Type a number: '))
    if c == 0:
        values.append(value_currently)
    elif c > 0:
        for j, v in enumerate(values):
            if value_currently < v:
                print(f'Value currently {value_currently} is less than {v} que está posição {j}')
                values.insert(j, value_currently)
                break
            elif value_currently > v:
                values.append(value_currently)
                break
print(values)

'''
Solução Guanabara

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
'''