# Mundo 2 - Desafio 044
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

valor_prod = float(input("Digite o valor do produto: "))
print("Certo! Temos as seguintes condições de pagamentos para você! :)")
print("1. À vista dinheiro/cheque: 10% de desconto)")
print("2. À vista no cartão: 5% de desconto)")
print("3. Em até 2x no cartão: preço normal")
print("4. 3x ou mais no cartão: 20% de juros")
op = int(input("Escolha um dessas opções acima: "))

if op == 1:
    valor_prod_d10 = valor_prod - valor_prod*0.1
    print("[OPÇÃO 1 ESCOLHIDA] - Valor do produto com 10% de desconto aplicado: {:.2f}".format(valor_prod_d10))
elif op == 2:
    valor_prod_d5 = valor_prod - valor_prod*0.05
    print("[OPÇÃO 2 ESCOLHIDA] - Valor do produto com 5% de desconto aplicado: {:.2f}".format(valor_prod_d5))
elif op == 3:
    print("[OPÇÃO 3 ESCOLHIDA] - Valor do produto (preço normal): {:.2f}".format(valor_prod))
elif op == 4:
    valor_prod_j20 = valor_prod + valor_prod*0.2
    qtd_parcelas = int(input("Digite a quantidade de parcelas: "))
    valor_parcela = valor_prod_j20/qtd_parcelas
    print("[OPÇÃO 4 ESCOLHIDA] - Valor do produto com 20% de juros aplicados: {:.2f}".format(valor_prod_j20))
    print("Quantidade de parcelas: {} | Valor de cada parcela: {:.2f}".format(qtd_parcelas, valor_parcela))
else:
    print("Opção inválida de pagamento. Tente novamente.")