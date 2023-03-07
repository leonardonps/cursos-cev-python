# Mundo - Desafio 070
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# a) qual é o total gasto na compra
# b) quantos produtos custam mais de R$1000
# c) qual é o nome do produto mais barato.

resp = 'S'
qtd_produtos_mais_mil = 0
gasto_total = 0
cont = 0

while resp == 'S':
    produto_atual_nome = str(input("Digite o nome do produto: "))
    produto_atual_preco = float(input("Agora, o preço do produto: R$"))

    cont += 1

    if cont == 1 or produto_atual_preco < produto_mais_barato_preco:
        produto_mais_barato_nome = produto_atual_nome
        produto_mais_barato_preco = produto_atual_preco


    if produto_atual_preco > 1000:
        qtd_produtos_mais_mil += 1

    gasto_total += produto_atual_preco

    resp = str(input("Deseja adicionar mais um produto no carrinho (S/N)? ")).strip().upper()[0]

    while resp not in 'SN':
        resp = str(input("Ooops... Opção inválida. Digite S (sim) ou N (não) para adicionar ou não mais um produto no carrinho: ")).strip().upper()[0]


print("=-="*20)
print(f"Gasto total na compra foi: R${gasto_total :.2f}")
print(f"Quantidade de produtos com mais de R$1000 comprados foi: {qtd_produtos_mais_mil}")
print(f"Produto mais barato comprado: {produto_mais_barato_nome}, que custa R${produto_mais_barato_preco :.2f}")




