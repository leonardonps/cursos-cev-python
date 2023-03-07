# Mundo - Desafio 065
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

soma = 0
qtd_numeros = 0
resp = 'S'
primeiro_numero = True

# while resp in 'Ss':
while resp == 'S':
    numero_atual = float(input("[{}] Digite um número: ".format(qtd_numeros+1)))

    if primeiro_numero:
        menor_numero = numero_atual
        maior_numero = numero_atual
        primeiro_numero = False
    else:
        if numero_atual < menor_numero:
            menor_numero = numero_atual
        if numero_atual > maior_numero:
            maior_numero = numero_atual

    soma += numero_atual
    qtd_numeros += 1
    resp = input("Deseja continuar?(S/N): ").upper()

print("")
print("O maior número encontrado foi: {:.2f}".format(maior_numero))
print("O menor número encontrado foi: {:.2f}".format(menor_numero))
print("A média entre os números foi: {:.2f}".format(soma/qtd_numeros))

