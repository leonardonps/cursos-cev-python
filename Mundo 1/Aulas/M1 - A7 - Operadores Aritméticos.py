n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end = '>>>')
print('Divisão inteira {} e potência {}'.format(di, e))

# O \n tem a mesma função como na linguagem C
# end = ' ' pode ser utilizado para juntar dois print em uma mesma linha
# {:.3f} para determinar  a quantidade de decimais de um número float