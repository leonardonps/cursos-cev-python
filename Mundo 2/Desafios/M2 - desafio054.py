# Mundo 2 - Mundo 054
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.

from datetime import date

ano_atual = date.today().year
maior_idade = 0
menor_idade = 0

for c in range(0, 7):
    print("[PESSOA {}]".format(c+1), end="")
    ano_nasc = int(input(" Digite seu ano de nascimento: "))
    if (ano_atual - ano_nasc) > 17:
        maior_idade = maior_idade + 1
    else:
        menor_idade = menor_idade + 1

print("Quantidade de pessoas de maior idade: {}".format(maior_idade))
print("Quantidade de pessoas de menor idade: {}".format(menor_idade))