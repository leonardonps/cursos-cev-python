# Mundo 2 - Desafio 050
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que foram pares. Se o valor
# digitado for ímpar, desconsidere-o.

soma = 0

for c in range(0, 6):
    num = int(input("[{}] Digite um número: ".format(c)))
    if num % 2 == 0:
        soma = soma + num

print("A soma total dos números que são pares deu: {}".format(soma))
