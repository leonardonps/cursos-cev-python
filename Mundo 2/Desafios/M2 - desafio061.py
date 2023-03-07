# Mundo - Desafio 061
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura WHILE.

acumulador = int(input("Digite o primeiro termo da PA: "))
razao_pa = int(input("Agora, a razão da PA: "))

contador = 0

while contador < 10:
    print("{}".format(acumulador), end=" ")
    if contador != 9:
        print("-> ", end="")
    acumulador = acumulador + razao_pa
    contador += 1