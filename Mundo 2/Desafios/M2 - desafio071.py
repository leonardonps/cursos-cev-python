# Mundo - Desafio 071
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input("Digite o valor a ser sacado: "))

qtd_50 = valor // 50
resto_qtd_50 = valor % 50

qtd_20 = resto_qtd_50 // 20
resto_qtd_20 = resto_qtd_50 % 20

qtd_10 = resto_qtd_20 // 10
resto_qtd_10 = resto_qtd_20 % 10

qtd_5 = resto_qtd_10 // 5
resto_qtd_5 = resto_qtd_10 % 5

qtd_1 = resto_qtd_5

print("=-="*15)

if qtd_50 > 0:
    print(f"Quantidade de cédulas de R$50: {qtd_50}")

if qtd_20 > 0:
    print(f"Quantidade de cédulas de R$20: {qtd_20}")

if qtd_10 > 0:
    print(f"Quantidade de cédulas de R$10: {qtd_10}")

if qtd_5 > 0:
    print(f"Quantidade de cédulas de R$5: {qtd_5}")

if qtd_1 > 0:
    print(f"Quantidade de cédulas de R$1: {qtd_1}")

print("=-="*15)

print("Obrigado! Volte sempre :)")

"""
Solução Guanabara

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))

total = valor
céd = 50
totcéd = 0

while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        
        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

"""
