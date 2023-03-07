# Mundo 3 - Desafio 074
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
menor_numero = numeros[0]
maior_numero = numeros[0]

for elemento in numeros:
    if elemento > maior_numero:
        maior_numero = elemento
    if elemento < menor_numero:
        menor_numero = elemento

print(f'Os cinco números aleatórios gerados foram: {numeros}')
print(f'O maior número gerado foi: {maior_numero}') # pode usar max(numeros)
print(f'O menor número gerado foi: {menor_numero}') # min(numeros)