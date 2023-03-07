# Mundo 1 - Desafio 027
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input('Digite seu nome completo: ')).strip()

nome_separado = nome.split()
qtd_nomes = len(nome_separado)

primeiro_nome = nome_separado[0]
ultimo_nome = nome_separado[qtd_nomes-1]

print('Seu primeiro nome é: {}'.format(primeiro_nome))
print('Seu último nome é: {}'.format(ultimo_nome))