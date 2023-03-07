# Mundo 1 - Desafio 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

#km hm dam m dm cm mm
valor = float(input("Digite o valor em metros: "))
km = valor/1000
hm = valor/100
dam = valor/10
dm = valor*10
cm = valor*100
mm = valor*1000

print("{}m vale: {}km, {}hm, {}dam, {}dm {}cm e {}mm".format(valor, km, hm, dam, dm, cm, mm))