# Mundo 2 - Desafio 056
# Desenvolve um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.


print("=-=" * 20)

idade_soma = 0
maior_idade_homem = 0
homem_mais_velho = ""
qtd_mulheres_menos_20 = 0

for c in range(0,4):
    print("[PESSOA {}]".format(c+1))
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M - masculino / F - Feminino): ")

    idade_soma = idade_soma + idade

    if sexo.upper() == "M" and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_mais_velho = nome

    if sexo.upper() == "F" and idade < 20:
        qtd_mulheres_menos_20 = qtd_mulheres_menos_20 + 1

    print("=-="*20)

print("A média de idade desse grupo é: {:.2f}".format(idade_soma/4))
if homem_mais_velho == "":
    print("Nome do homem mais velho: nenhuma pessoa foi registrada com o sexo masculino.")
else:
    print("Nome do homem mais velho: {}".format(homem_mais_velho))
print("Quantidade de mulheres que têm menos 20 anos: {}".format(qtd_mulheres_menos_20))



