# Mundo 1 - Desafio 025
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o seu nome completo: ')).strip()

nome = nome.upper()

tem_silva = 'SILVA' in nome

print('Seu nome tem SILVA nele: {}'.format(tem_silva))
