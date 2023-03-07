# Mundo 2 - Desafio 055
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

for c in range(0, 5):
    print("[PESSOA {}]".format(c+1), end="")
    peso = float(input(" Digite seu peso: "))

    if c == 0:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso

print("Maior peso lido: {:.2f}kg".format(maior_peso))
print("Menor peso lido: {:.2f}kg".format(menor_peso))

