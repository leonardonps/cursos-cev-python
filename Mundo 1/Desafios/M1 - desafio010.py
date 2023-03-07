# Mundo 1 - Desafio 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1.00 = R$3.27

dinheiro = float(input("Digite a quantidade de dinheiro: R$"))
dol = dinheiro / 5.16

print("R${} em dólares é igual a U${:.4f}".format(dinheiro, dol))
