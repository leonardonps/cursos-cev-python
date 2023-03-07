# Mundo - Desafio 060
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex.: 5! = 5x4x3x2x1 = 120
# Faça usando WHILE e FOR

num = int(input("Digite um número para saber seu fatorial: "))
fatorial = 1

num_rotativo = num

while num_rotativo > 0:
    fatorial = fatorial * num_rotativo
    num_rotativo -= 1

print("O fatorial do número {} é: {}".format(num, fatorial))

#fatorial = 1

#for num_rotativo in range(num, 0, -1):
#    fatorial = fatorial * num_rotativo
#print("O fatorial do número {} é: {}".format(num, fatorial))