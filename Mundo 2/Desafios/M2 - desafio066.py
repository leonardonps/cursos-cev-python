# Mundo - Desafio 066
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag)

qtd_numeros = soma = 0

while True:
    num_atual = int(input("Digite um número inteiro [999 para parar]: "))
    if num_atual == 999:
        break
    soma += num_atual
    qtd_numeros += 1

print("=-=" * 20)
print(f"Quantidade de números: {qtd_numeros}")
print(f"A soma total entre os números: {soma}")
