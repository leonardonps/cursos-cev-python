# Mundo 1 - Desafio 011
# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('Digite a largura em metros: '))
alt = float(input('Digite a altura em metros: '))
area = larg * alt
qtdTinta = area/2
print('A área dessa parede, com dimensão {}mx{}m, é: {} m² e precisará de {:.2f} litros de tinta para ser pintada.'.format(larg, alt, area, qtdTinta))