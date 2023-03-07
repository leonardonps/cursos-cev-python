# Mundo 1 - Desafio 006
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input("Digite um número:"))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)


print("Número {}: ".format(num))
print("DOBRO: {}".format(dobro))
print("TRIPLO: {}".format(triplo))
print("RAIZ: {:.2f}".format(raiz))
#pow(n, (1/2))
