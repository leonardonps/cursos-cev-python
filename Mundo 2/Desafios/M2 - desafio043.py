# Mundo 2 - Desafio 043
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# bela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

valor_imc = peso/(altura*altura)

if valor_imc < 18.5:
    print("O valor do seu IMC é: {:.2f}. Está abaixo do peso.".format(valor_imc))
elif 18.5 <= valor_imc <= 24.9:
    print("O valor do seu IMC é {:.2f}. Está com o peso ideal.".format(valor_imc))
elif 25 <= valor_imc <= 29.9:
    print("O valor do seu IMC é {:.2f}. Está com sobrepeso.".format(valor_imc))
elif 30 <= valor_imc <= 40:
    print("O valor do seu IMC é {:.2f}. Está com obesidade.".format(valor_imc))
elif valor_imc > 40:
    print("O valor do seu IMC é {:.2f}. Está com obesidade mórbida.".format(valor_imc))