# Mundo 1 - Desafio032
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date

ano = int(input("Digite o ano para se é bissexto ou não (Coloque 0 para calcular o ano atual): "))

if ano == 0:
    ano = date.today().year

if ano % 100 == 0 and ano % 400 == 0:
    print("{} é um ano bissexto.".format(ano))
else:
    if ano % 4 == 0 and ano % 100 != 0:
        print("{} é um ano bissexto.".format(ano))
    else:
        print("{} não é ano bissexto.".format(ano))

'''
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
'''