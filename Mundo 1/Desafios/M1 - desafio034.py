# Mundo 1 - Desafio 034
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
# a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o salário: "))

if salario > 1250:
    salario_nv = salario + salario*0.1
else:
    salario_nv = salario + salario*0.15

print("O salário anterior: R${:.2f}".format(salario))
print("Agora, é de: R${:.2f}".format(salario_nv))
