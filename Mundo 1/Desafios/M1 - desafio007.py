# Mundo 1 - Desafio 007
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

# Variáveis em Python pode ser definidas com acentos. Exemplo: média
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2)/2

print("========================")
print("Nota 1: {:.2f}".format(n1))
print("Nota 2: {:.2f}".format(n2))
print("------------------------")
print("A media das notas é: {:.2f}".format(media))
print("========================")