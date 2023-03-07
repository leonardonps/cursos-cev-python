# Mundo 1 - Desafio 026
# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()

frase = frase.upper()

qtd_a = frase.count('A')
primeiro_a = frase.find('A')
ultimo_a = frase.rfind('A')

print('Tem {} a\'s nessa frase.'.format(qtd_a))
print('O primeiro A está na posição: {}.'.format(primeiro_a))
print('O último A está na posição: {}.'.format(ultimo_a))

