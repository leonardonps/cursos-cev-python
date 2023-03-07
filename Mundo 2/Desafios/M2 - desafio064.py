# Mundo - Desafio 064
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando a flag)

valor_flag = 0
soma = 0
qtd_numeros = 0

numero_atual = 0

while numero_atual != 999:
    numero_atual = int(input("Digite um número para ser somado [Digite 999 para parar]: "))
    if numero_atual != 999:
        soma += numero_atual
        qtd_numeros += 1

"""
Sem usar IF dentro do WHILE

numero_atual = int(input("Digite um número para ser somado [Digite 999 para parar]: "))

while numero_atual != 999:
    soma += numero_atual
    qtd_numeros += 1
    numero_atual = int(input("Digite um número para ser somado [Digite 999 para parar]: "))

"""

"""
Usando comando Break

while True:
    numero_atual = int(input("Digite um número para ser somado [Digite 999 para parar]: "))
    
    if numero_atual == 999:
        break
    
    soma += numero_atual
    qtd_numeros += 1
"""

print("A quantidade de números foi: {} e a soma entre eles é: {}".format(qtd_numeros, soma))
# print(f'A soma vale {soma}')