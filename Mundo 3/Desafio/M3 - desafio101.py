# Mundo 3 - Desafio 101
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def vote(birth_year):
    """
    -> Simple function that determinates if a person's vote is negated, optional or obligated
    :param birth_year: year of birth of a person
    :return: this function returns a string informing if the vote is negated, optional or obligated
    """
    from datetime import datetime

    current_year = datetime.now().year
    age = current_year - birth_year

    print(f'Your age: {age} years old')

    if age < 16:
        return 'Vote is NEGATED'
    elif (age >= 16 and age < 18 ) or age > 70:
        return 'Vote is OPTIONAL'
    else:
        return 'Vote is OBLIGATED'

# Main program

birth_year = int(input('Type your year of birth: '))

print(vote(birth_year))

