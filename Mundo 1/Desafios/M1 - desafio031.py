# Mundo 1 - Desafio 031
# Desenvolve um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km
# para viagens de até 200Km e R$0,45 para viagens mais longas.

dist = float(input("Digite a distância percorrida em km: "))

if dist > 200:
    taxa_200_mais = dist * 0.45
    print("O preço da passagem é de: R${:.2f}".format(taxa_200_mais))
else:
    taxa_200 = dist * 0.5
    print("O preço da passagem é de: R${:.2f}".format(taxa_200))

'''
distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('E o preço da sua passagem será de R${:.2f}'.format(preco))
'''

'''
if-line / operador ternario

preco =  distancia * 0.50 if distancia <= 200 else distancia * 0.45
'''