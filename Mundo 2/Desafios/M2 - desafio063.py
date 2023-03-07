# Mundo - Desafio 063
# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência
# de Fibonacci.
# Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

qtd_elementos = int(input("Digite a quantidade de elementos que você quer ver da sequência de Fibonacci: "))

index_elemento = 3
valor_index_anterior = 1
valor_index_anteanterior = 0

# index_elemento == 0
print("0", end=" ")

# index_elemento == 1
print("-> 1", end=" ")

#index_elemento >= 3
while index_elemento <= qtd_elementos:
    valor_index_atual = valor_index_anteanterior + valor_index_anterior
    print("-> {}".format(valor_index_atual), end=" ")

    valor_index_anteanterior = valor_index_anterior
    valor_index_anterior = valor_index_atual

    index_elemento +=1