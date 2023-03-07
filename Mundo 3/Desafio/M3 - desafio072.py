# Mundo 3 - Desafio 072
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até 20.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


resp = 'S'
while resp == 'S':
    num_escolhido = int(input("Digite o número entre 0 e 20 para saber como se escreve por extenso: "))
    while num_escolhido < 0 or num_escolhido > 20:
        num_escolhido = int(input("Ooops! Número inválido. Tente novamente, digite um número entre 0 e 20"
                                  " para saber como se escreve por extenso: "))

    print(f"O número {num_escolhido} por extenso é: {numeros[num_escolhido]}")


    resp = str(input('Quer saber de outro número [s/n]? ')).strip().upper()[0]

    while resp not in 'SN':
        resp = str(input('Opção inválida. Digite S para sim ou N para Não: ')).strip().upper()[0]
"""
Solução Guanabara
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitoou o número{cont[]}')
"""