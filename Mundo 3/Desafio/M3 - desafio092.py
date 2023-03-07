# Mundo 3 - Desafio 092
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de zero, o dicionário receberá o ano de contratação e o salário. Calcule e acrescente
# além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

data_user = dict()

data_user["Name"] = str(input('Type your name: '))
data_user["Age"] = date.today().year - int(input("Now, year of your birth: "))
data_user["Work card"] = int(input("At last, work card (if you don't have it, type 0): "))

if  data_user.get("Work card") > 0:
    print('Ok, your basic data are registered. Now, give us some other informations: ')
    data_user["Year of hire"] = int(input('Year of hire: '))

    current_year = date.today().year
    worked_time = current_year - data_user.get('Year of hire')
    time_to_work = 35 - worked_time
    data_user["Retirement age"] = data_user.get("Age") + time_to_work
    data_user["Salary"] = float(input('Salary: '))

print('-='*20)
for k, v in data_user.items():
    print(f'{k}: {v}')