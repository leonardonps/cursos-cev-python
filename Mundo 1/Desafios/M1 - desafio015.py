# Mundo 1 - Desafio 015
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
# o carro custa R$60 por dia e R$0,15 por km rodado.

km = float(input('Quantos quilometros foram percorridos pelo carro?'))
dias = int(input('Por quantos dias o carro ficou alugado?'))

valKm = km * 0.15
valDias = dias * 60

total = valKm + valDias

print('=='*30)
print('Valor cobrado pelos quilometros percorridos: R${:.2f}.'.format(valKm))
print('Valor cobrado pelos dias alugados: R${}.'.format(valDias))
print('-'*60)
print('Certo! O valor total do aluguel do carro deu: R${:.2f}.'.format(total))
print('=='*30)
