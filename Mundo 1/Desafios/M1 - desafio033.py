# Mundo 1 - Desafio 033
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Agora, o segundo número: "))
n3 = int(input("Por último, o terceiro número: "))

if n1 > n2 and n1 > n3:
    num_maior = n1
if n2 > n1 and n2 > n3:
    num_maior = n2
if n3 > n1 and n3 > n2:
    num_maior = n3

if n1 < n2 and n1 < n3:
    num_menor = n1
if n2 < n1 and n2 < n3:
    num_menor = n2
if n3 < n1 and n3 < n2:
    num_menor = n3

'''
menor = a
if b < a and b < c:
    menor = b
if c<a and c<b:
    menor = c

maior = a 
if b > a and b > c:
    maior = a
if c > a and c > b:
    maior = c
'''

print("O maior número entre os três digitados é: {}. Já o menor número é: {}.".format(num_maior, num_menor))