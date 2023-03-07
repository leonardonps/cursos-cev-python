# Mundo 3 - Desafio 076
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
# No final, mostre uma listagem de preços organizando os dados em forma tabular.

produtos = ('Café', 7.99, 'Açúcar', 4.25, 'Arroz', 6.00, 'Macarrão', 3.25)

print('{:^50}'.format('Lista de produtos'))

for elemento in produtos:
    if produtos.index(elemento) % 2 == 0:
        print('{:.<40}'.format(elemento), end=" ")
    else:
        print('R$ {:.2f}'.format(elemento))

#  Solução Guanabara
#
# for pos in range (0, len(produtos)):
#     if pos % 2 == 0:
#         print(f'{produtos[pos]:.<30}', end='')
#     else:
#         print(f'R${produtos[pos]:>7.2f}')