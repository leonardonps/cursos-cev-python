# Mundo 1 - Desafio 023
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex.: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numero_usuario = int(input('Digite um número de 0 a 9999: '))

print('Analisando o número: {}...'.format(numero_usuario))

milhar = numero_usuario//1000
resto_milhar = numero_usuario%1000
# m = num // 1000 % 10

centena = resto_milhar//100
resto_centena = resto_milhar%100
# c = num // 100 % 10

dezena = resto_centena//10
resto_dezena = resto_centena%10
# d = num // 10 % 10

unidade = resto_dezena
# u = num // 1 % 10

print('Unidade: {}'.format(unidade))
print('Dezena:  {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar:  {}'.format(milhar))
