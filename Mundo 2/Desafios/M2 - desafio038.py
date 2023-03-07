# Mundo 2 - Desafio 038
# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))

if primeiro_valor > segundo_valor:
    print("{} é maior que {}".format(primeiro_valor, segundo_valor))
elif segundo_valor > primeiro_valor:
    print("{} é maior que {}".format(segundo_valor, primeiro_valor))
else:
    print("{} e {} são iguais".format(primeiro_valor, segundo_valor))
