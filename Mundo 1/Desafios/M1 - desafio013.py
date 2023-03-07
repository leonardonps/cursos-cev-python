# Mundo 1 - Desafio 013
# Faça um algoritmo que leia o salário e mostre seu novo saláro com 15% de aumento

sal = float(input('Digite o valor do salário a ser aplicado: R$'))
sal = sal + sal*0.15
print('O valor do salário aumentado é: {:.2f}'.format(sal))