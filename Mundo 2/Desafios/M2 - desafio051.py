# Mundo 2 - Desafio 051
# Desenvolva um programa que leia o primeiro termo e razão de um PA. No final, mostre os 10 primeiros termos desssa
# progressão.

primeiro_termo = int(input("Digite o primeiro termo: "))
razao_pa = int(input("Digite agora a razão da progressão aritmética: "))

for c in range(1, 11):
    termo = primeiro_termo + (c - 1) * razao_pa
    print(termo)

'''
Solução Guanabara

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão

for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end="=> "):
print('ACABOU')    



'''