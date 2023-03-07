# Mundo 1 - Desafio 024
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

nome_cidade = str(input('Digite o nome de uma cidade: ')).strip()
nome_cidade_separado = nome_cidade.split(" ")
primeiro_nome = nome_cidade_separado[0]

primeiro_nome = primeiro_nome.upper()

tem_santo = primeiro_nome == "SANTO"

print('Essa cidade começa com \'Santo\': {}'.format(tem_santo))
