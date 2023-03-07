# Mundo 3 - Desafio 077
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais.

paises = ('Brasil', 'Argentina', 'Paraguai', 'Uruguai', 'Chile', 'Venezuela', 'Colombia', 'Bolivia', 'Equador', 'Guiana Francesa', 'Guiana', 'Suriname', 'Peru')
for pais in paises:
    print(f'O país {pais} tem as seguintes vogais:', end=" " )
    for letra in pais:
        if letra.lower() in 'aeiou':
            print(letra, end=" ")
    print('')
