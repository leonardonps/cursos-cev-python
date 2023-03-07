# Mundo 2 - Desafio 048
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.

soma = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            print(c)
            soma = soma + c

print(soma)


'''
Solução Guanabara

for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
         cont += 1
print("A soma de todos os {} valores solicitados é {}".format(cont, soma))

'''