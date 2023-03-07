# Mundo 3 - Desafio 078
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
pos_max_valor = []
pos_min_valor = []

for c in range(0, 5):
    valores.append(int(input(f'[{c+1}] Digite um valor: ')))

    if c == 0:
        max_valor = min_valor = valores[c]
    else:
        if valores[c] > max_valor:
            max_valor = valores[c]

        if valores[c] < min_valor:
            min_valor = valores[c]

for c, v in enumerate(valores):
    if v == max_valor:
        pos_max_valor.append(c)
    if v == min_valor:
        pos_min_valor.append(c)


print(f'O maior valor nessa lista é: {max_valor} | Posições {pos_max_valor}') # max(valores)
print(f'O menor valor nessa lista é: {min_valor} | Posições {pos_min_valor}') # min(valores)