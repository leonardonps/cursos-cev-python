def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

# * empacatador = pega todos os parâmetros que a pessoa passa e coloca em um pacote de parâmetros
def contador(*núm):
    for valor in núm:
        print(f'{valor}', end=' ')
    print('FIM!')
# Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
contador(1, 2, 3, 4, 5)

