# Mundo 1 - Desafio 035
# Desenvolve um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

lado_a = float(input("Digite o primeiro lado: "))
lado_b = float(input("Digite o segundo lado:  "))
lado_c = float(input("Digite o terceiro lado: "))

soma_bc = lado_b + lado_c
soma_ac = lado_a + lado_c
soma_ab = lado_a + lado_b

dif_bc = lado_b - lado_c
dif_ac = lado_a - lado_c
dif_ab = lado_a - lado_b

if (abs(dif_bc) < lado_a < soma_bc) and (abs(dif_ac) < lado_b < soma_ac) and (abs(dif_ab) < lado_c < soma_ab):
    print("A junção das retas: {}, {} e {} é um triangulo!".format(lado_a, lado_b, lado_c))
else:
    print("A junção das retas: {}, {} e {} não é um triangulo.".format(lado_a, lado_b, lado_c))

