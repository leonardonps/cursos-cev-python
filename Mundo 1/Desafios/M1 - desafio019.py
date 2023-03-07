# Mundo 1 - Desafio 019
# Um professor quer sortear um dos seus quatro alunos para
# apagar o quadro. Faça um programa que ajude ele, lendo
# o nome deles e escrevendo o nome do escolhido.

import random
#from random import choice

a1 = str(input('Digite o primeiro aluno:'))
a2 = str(input('Digite o segundo aluno:'))
a3 = str(input('Digite o terceiro aluno:'))
a4 = str(input('Digite o quarto aluno:'))

alunos = [a1, a2, a3, a4]
alunoSort = random.choice(alunos)

print('O aluno sorteado foi: {}'.format(alunoSort))
