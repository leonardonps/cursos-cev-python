# Mundo 1 - Desafio 014
# Faça um algoritmo que converta a temperatura de Celsius para Fahrenheit

tempC = float(input('Informe a temperatura em ºC: '))
#Nesse caso específico, não precisa dos parenteses pois a ordem de precedencia já deixa a conta correta
#tempF = ((9*tempC)/5) + 32
tempF = tempC*1.8 + 32
print('A temperatura de {:.2f}ºC corresponde a {:.2f}ºF!'.format(tempC, tempF))