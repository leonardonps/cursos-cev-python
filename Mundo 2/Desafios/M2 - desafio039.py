# Mundo 2 - Desafio 039
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

sexo = input("Digite seu sexo - (M) Masculino ou F (Feminino): ")

if sexo.upper() == 'M':

    ano_nasc = int(input("Digite seu ano de nascimento: "))
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc

    if idade == 18:
        print("Você completará {} anos esse ano. Logo, terá que se alistar ao serviço militar.".format(idade))
    elif idade < 18:
        tempo_falta = 18 - idade
        ano_alistamento = ano_atual + tempo_falta
        print("Você tem {} anos. Ainda falta {} ano(s) para se alistar ao serviço militar. Ano de alistamento: {}".format(idade, tempo_falta, ano_alistamento))
    elif idade > 18:
        tempo_passou = idade - 18
        ano_alistamento = ano_atual - tempo_passou
        print("Você tem {} anos. Você deveria ter se alistado há {} ano(s) atrás. Ano do alistamento: {}".format(idade, tempo_passou, ano_alistamento))

elif sexo.upper() == 'F':
    print("O serviço militar não é obrigatório para você.")
else:
    print("Opção inválida. Tente novamente.")