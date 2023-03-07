# Mundo 3 - Desafio 075
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os números pares.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Agora, o terceiro número: '))
n4 = int(input('Por último, o quarto número: '))

numeros = (n1, n2, n3, n4)

"""
Forma de Guanabara

numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
 int(input('Agora, o terceiro número: ')), int(input('Por último, o quarto número: ')))

"""

print('==='*20)
print(f"Quantidade de vezes que o 9 foi digitado: {numeros.count(9)}")

print("Posição do primeiro valor 3 digitado: ", end="")

# if 3 in numeros: else:
if numeros.count(3) == 0:
    print("nenhum número 3 foi digitado.")
else:
    print(numeros.index(3) + 1)

print("Números pares digitados: ", end="")

for elemento in numeros:
    if elemento % 2 == 0:
        print(elemento, end=" ")