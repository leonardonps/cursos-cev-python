# Mundo 2 - Desafio 052
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite um número para saber se é primo: "))
cont_divisao = 0

for c in range(1,num+1):
    if num % c == 0:
        cont_divisao = cont_divisao + 1

if cont_divisao != 2:
    print("O número {} NÃO é PRIMO.".format(num))
else:
    print("O número {} é PRIMO.".format(num))


'''
Solução Guanabara

num = int(input('Digite um numero: '))
tot = 0 

for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))

if tot == 2:
    print('E por isso ele é PRIMO!')
else: 
    print('E por isso ele NÃO É PRIMO!')
'''