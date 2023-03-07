# Mundo 1 - Desafio 004
# Faça um programa que leia algo pelo teclado e mostre o seu tipo primitivo e todas as informações possíveis sobre ele.

var = input("Digite alguma coisa: ")
print("O tipo primitivo da coisa digitada é : ", type(var))
print("É um número? ", var.isnumeric())
print("Tem decimal? ", var.isdecimal())
print("Pode ser representado pelo ASCII? ", var.isascii())
print("Está no alfabeto? ", var.isalpha())
print("É alfanumérico? ", var.isalnum())
print("Está tudo em minisculo? ", var.islower())
print("Está tudo em maisculo? ", var.isupper())
print("Só tem espaços? ", var.isspace())
print("Está capitalizada? ", var.istitle())