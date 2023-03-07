# Mundo - Desafio 062
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 termos.

acumulador = int(input("Digite o primeiro termo da PA: "))
razao_pa = int(input("Agora, a razão da PA: "))


qtd_termos = 10

while qtd_termos != 0:
    contador = 0
    while contador < qtd_termos:
        print("{}".format(acumulador), end=" ")
        if contador != qtd_termos-1:
            print("-> ", end="")
        acumulador = acumulador + razao_pa
        contador += 1
    print("")
    qtd_termos = int(input("Você deseja acrescentar mais termos? (Se sim, digite a quantidade. Se não, digite 0): "))