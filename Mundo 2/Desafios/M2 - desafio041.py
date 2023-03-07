# Mundo 2 - Desafio 041
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de uma atleta e mostre sua categoria,
# de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

import datetime

ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = datetime.date.today().year

idade = ano_atual - ano_nasc

if idade < 10:
    print("Você tem {} anos. Está na categoria MIRIM.".format(idade))
elif 9 < idade < 15:
    print("Você tem {} anos. Está na categoria INFANTIL.".format(idade))
elif 14 < idade < 21:
    print("Você tem {} anos. Está na categoria SÊNIOR.".format(idade))
elif idade > 20:
    print("Você tem {} anos. Está na categoria MASTER.".format(idade))


