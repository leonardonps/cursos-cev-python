# Mundo 3 - Desafio 090
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
# conteúdo da estrutura na tela.

student = {}

student['Name'] = str(input("Type student's name: "))
student['Average'] = float(input(f"Type {student['Name']}'s average: "))

if student['Average'] >= 7:
    student['Situation'] = 'Approved'
else:
    student['Situation'] = 'Recovery'

print()
print('{:^20}'.format("======= Student's data ======="))

for k, v in student.items():
    print(f'{k}: {v}')