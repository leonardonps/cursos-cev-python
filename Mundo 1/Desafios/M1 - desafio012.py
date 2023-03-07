# Mundo 1 - Desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prodPreco = float(input('Digite o preço, em reais, do produto ao qual será aplicado o desconto:R$ '))
prodPreco = prodPreco - prodPreco*0.05
print('O novo valor do produto é: {:.2f} reais'.format(prodPreco))