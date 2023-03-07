# Mundo 3 - Desafio 106
# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar, a palavra 'FIM', o programa se encerrará.
# Obs.: Use cores.

print('-='*35)
print('{:^80}'.format('\033[100mWelcome to Helping in Python Program :)\033[00m'))
print('-='*35)
print("\033[31mObservation: type 'Exit' if you want to exit of this program\033[00m")
print('-'*70)
print('')

while True:
    word = str(input("\033[36mType a command to see in the Python's Interactive Help: \033[m"))
    if word.upper() == 'Exit':
        break
    print('\033[97;40m')
    help(word)
    print('\033[m')
