# Mundo 2 - Desafio 040
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
# média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1+nota_2)/2.0

if media < 5.0:
    print("O aluno foi REPROVADO. Sua média é: {:.2f}".format(media))
elif 5.0 <= media < 7:
    print("O aluno está em RECUPERAÇÃO. Sua média atual é: {:.2f}".format(media))
elif media >= 7.0:
    print("O aluno foi APROVADO com média igual a {:.2f}".format(media))