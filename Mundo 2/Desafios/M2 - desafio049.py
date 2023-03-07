# Mundo 2 - Desafio 049
# Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input("Digite um número para fazer sua tabuada: "))

for c in range (0, 11):
    print("{:2} x {} = {}".format(c, num, c*num))
