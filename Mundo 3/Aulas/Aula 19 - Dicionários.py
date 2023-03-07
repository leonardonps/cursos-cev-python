pessoas = {'nome': 'Gustavo',
           'sexo': 'M',
           'idade': 22}

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.96

# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())

for el in pessoas.keys():
    print(el)
for el in pessoas.values():
    print(el)
for k, el in pessoas.items():
    print(f'{k} = {el}')

brasil = []

estado1 = { 'uf': 'Rio de Janeiro',
            'sigla': 'RJ'}

estado2 = {'uf': 'São Paulo',
           'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

# print(brasil[0]['uf'])
# print(brasil[0]['sigla'])

estado = dict()
brasil = list()

for c in range (0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
    for v in e.values():
        print(v, end=" ")
    print()