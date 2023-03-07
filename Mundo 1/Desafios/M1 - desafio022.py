# Mundo 1 - Desafio 022
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Nome completo todo maiusculo: {}'.format(nome.upper()))
print('Nome completo todo minusculo: {}'.format(nome.lower()))

nome_separado = nome.split(" ")
print('Seu primeiro nome \'{}\' tem: {} letras.'.format(nome_separado[0], len(nome_separado[0])))

nome_junto = nome.replace(" ", "")
print('Seu nome completo tem: {} letras.'.format(len(nome_junto)))
# print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# Por exemplo se for ANA CAROL (012 3 45678), o espaço vai ser o terceiro elemento (porque começa com 0),
# logo temos 3 casas antes, ou seja, o nome tem 3 letras
