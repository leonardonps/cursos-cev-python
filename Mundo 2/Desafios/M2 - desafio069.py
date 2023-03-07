# Mundo - Desafio 69
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
# o usuário quer ou não continuar. No final, mostre:
# a) quantas pessoas tem mais de 18 anos
# b) quantos homens foram cadastrados
# c) quantas mulheres tem menos de 20 anos

pessoas_mais_18 = homens = mulheres_menos_20 = 0

while True:
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()[0]

    idade = int(input("Agora, sua idade: "))

    if idade > 18:
        pessoas_mais_18 += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    resp = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]

    while resp not in 'SN':
        resp = str(input("Por favor, digite uma opção válida [S - SIM | N - NÃO]: ")).strip().upper()[0]

    if resp == 'N':
        break

print(f"Quantidade de pessoas maiores de 18 anos: {pessoas_mais_18}")
print(f"Quantidade de homens cadastrados: {homens}")
print(f"Quantidade de mulheres menores de 20 anos: {mulheres_menos_20}")
