# Mundo 3 - Desafio 097
# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.
# Ex.: escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~~~~~

def write(message):
    print('~' * (len(message) + 2))
    print(f' {message} ')
    print('~' * (len(message) + 2))

write('Python, you are cool. Did you know it?')