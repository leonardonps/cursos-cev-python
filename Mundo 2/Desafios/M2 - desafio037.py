# Mundo 2 - Desafio 037
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

valor_int = int(input("Digite o valor inteiro a ser convertido: "))

print("Digite agora para qual base você vai converter: ")

resposta = int(input("Digite:\n- 1 para binário\n- 2 para octal\n- 3 para hexadecimal\n"))

if resposta == 1:
    valor_bin = bin(valor_int)
    print("O número {} em binário é: {}".format(valor_int, valor_bin))
elif resposta == 2:
    valor_octal = oct(valor_int)
    print("O número {} em octal é: {}".format(valor_int, valor_octal))
elif resposta == 3:
    valor_hexa = hex(valor_int)
    print("O número {} em hex é: {}".format(valor_int, valor_hexa))
else:
    print("Opção inválida. Digite uma opção correta, por favor.")
