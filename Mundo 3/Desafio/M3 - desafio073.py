# Mundo 3 - Desafio 073
# Crie um tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois, mostre:
# a) Apenas os 5 primeiros colocados da tabela
# b) Os últimos 4 colocados da tabela.
# c) Uma lista com os times em ordem alfabética
# d) Em que posição na tabela está o time da Chapecoense (Não tem, vou colocar São Paulo)

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza',
         'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atletico-GO',
        'Avaí', 'Juventude')

print(f'Os cinco primeiros colocados são: {times[0:5]}')
print(f'Os quatro últimos colocados são: {times[16:20]}') # times[-4:]
print(f'Os times em ordem alfabética: {sorted(times)}')
print(f'Posição do time de São Paulo: {times.index("São Paulo")+1}')