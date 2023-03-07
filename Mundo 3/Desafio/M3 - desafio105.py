# Mundo 3 - Desafio 105
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com
# as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstring da função

def grades(*grades, situation=False):

    """
    This function receives a group of grades and calculates: the highest grade, the lowest grade,
    average of class and its situation
    :param grades: this parameter receives variable number of grades
    :param situation: this parameter determinates if we want to see or not the class's situation
    :return: the function returns a dictionary containing: the number of grades, the highest grade,
     the lowest grade, class's average and class's situation
    """

    class_grades = {
        'number_of_grades': len(grades),
        'highest_grade': max(grades),
        'lowest_grade': min(grades),
    }

    sum = avg = 0
    for g in grades:
        sum += g

    avg = sum / len(grades)

    class_grades['average'] = avg

    if situation == True:
        if avg < 6:
            class_grades['situation'] = 'Bad'
        elif 6 <= avg <= 8:
            class_grades['situation'] = 'Razoable'
        else:
            class_grades['situation'] = 'Good'

    return class_grades

# Main program
print(grades(8.1, 8.1, 8.1, 8.1, 100))