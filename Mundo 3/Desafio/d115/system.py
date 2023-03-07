# Mundo 3 - Desafio 115
# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um file de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
import utilidadesCeV.dado
import d115.interface
import d115.file
from time import sleep

fileName = "dados.txt"

if not d115.file.isFile(fileName):
    d115.file.createFile(fileName)

while True:
    d115.interface.header("PRS - People Registration System")
    d115.interface.menu(['Register a person', 'List of people', 'Exit'])
    d115.interface.line()

    op = utilidadesCeV.dado.readInt('Choose one of these options above: ')
    if op == 1:
        d115.interface.header("New person")
        d115.file.registerPerson(fileName)
    elif op == 2:
        d115.interface.header("Registered People")
        d115.file.readPeople(fileName)
    elif op == 3:
        d115.interface.header("Exit")
        print('...')
        sleep(0.5)
        print('\33[36mThanks for using our system :)\33[m')
        break
    else:
        print('\33[31mPlease, type a valid option.\33[m')
        input('')
