# Mundo 2 - Desafio 036
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Digite o valor da casa: R$"))
valor_salario = float(input("Digite o valor do salário: R$"))
emprestimo_anos = int(input("Digite em quantos anos você pagará essa casa: "))

prestacao_mensal = valor_casa/(emprestimo_anos*12)

if prestacao_mensal > valor_salario*0.3:
    print("O empréstimo foi negado porque a prestação mensal (R${:.2f}) excedeu 30% do salário declarado.".format(prestacao_mensal))
else:
    print("Parabéns! O empréstimo foi aprovado. A prestaçao mensal ficará por: R${:.2f}".format(prestacao_mensal))
