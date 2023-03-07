# Mundo 2 - Desafio 042
# Refaça o DESAFIO 035 dos triângulos, acrescentação o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

lado_a = float(input("Digite o lado A: "))
lado_b = float(input("Agora, o lado B: "))
lado_c = float(input("Por último, o lado C: "))

soma_bc = lado_b + lado_c
soma_ac = lado_a + lado_c
soma_ab = lado_a + lado_b

dif_bc = lado_b - lado_c
dif_ac = lado_a - lado_c
dif_ab = lado_a - lado_b


if abs(dif_bc) < lado_a < soma_bc and abs(dif_ac) < lado_b < soma_ac and abs(dif_ab) < lado_c < soma_ab:
    if lado_a == lado_b == lado_c:
        tipo_triangulo = "Equilátero"
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        tipo_triangulo = "Isósceles"
    elif lado_a != lado_b != lado_c != lado_a:
        tipo_triangulo = "Escaleno"
    print("------")
    print("Os três lados conseguem formar um triângulo. Tipo: {}.".format(tipo_triangulo))
else:
    print("Os três lados não conseguem formar um triângulo.")