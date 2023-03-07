# Mundo 2 - Desafio 053
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input("Digite uma frase para saber se ela é ou não palíndroma: ")
frase_separada = frase.lower().split()
print(frase_separada)
frase_junta = "".join(frase_separada)

print(frase_junta)

if frase_junta == frase_junta[::-1]:
    print("A frase {} é PALÍNDROMA".format(frase))

'''
Solução Guanabara

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(lent(junto) -1, -1, -1)
    inverso += junto[letra]

print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada nãoé um palíndromo!')

OUTRA SOLUÇÃO:

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada nãoé um palíndromo!')

'''