# Mundo 1 - Desafio 029
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Digite a velocidade, em km/h, do carro para calcular a multa: "))

if velocidade > 80:
    print("A velocidade está acima da permitida. Por isso, você será multado.")
    km_acima = velocidade- 80
    multa = km_acima * 7
    print("Você pagará R${} pois estava acima do permitido.".format(multa))
else:
    print("Você está dentro do limite permitido. Não receberá nenhuma multa.")


