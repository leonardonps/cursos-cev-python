# Mundo 3 - Desafio 089
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

grades = list()
student = list()
students = list()

while True:
    name = str(input("Type the student's name: "))
    grade_1 = float(input('Type grade 1: '))
    grade_2 = float(input('Now, grade 2: '))

    student.append(name)
    grades.append(grade_1)
    grades.append(grade_2)

    print(student)

    average = (grade_1 + grade_2)/2

    student.append(grades[:])
    student.append(average)

    print(student)

    students.append(student[:])

    grades.clear()
    student.clear()

    ans = str(input('Would you like to add another student [Y/N]? ')).strip().upper()[0]
    while ans not in 'YN':
        ans = str(input('Sorry, type a valid option. Y for yes or N for no: ')).strip().upper()[0]
    if ans == 'N':
        break

print('')
print('{:^60}'.format('Students'))
print('=-'*30)
for c, s in enumerate(students):
    print(f'Identification number: {c+1}')
    print(f"Student's name: {s[0]}")
    print(f"Average: {s[2]:.2f}")
    print('=-'*30)

while True:
    id_student = int(input('Would you like to see the grades detaily of a student? '
                           'Type the identification number to it or 999 to exit: '))
    if id_student == 999:
        break

    for c, s in enumerate(students):
        if c == (id_student - 1):
            print(f"Student's name: {s[0]}")
            print(f'Grade 1: {s[1][0]}')
            print(f'Grade 2: {s[1][1]}')