# Tuplas são imutáveis
# Apesar de serem imutáveis, podemos apagá-las usando o comando 'del'. Exemplo: del(pessoa)
# Variáveis compostas em Python
# () - Tuplas, [] - Listas, {} - Dicionário

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

#for cont in range (0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]}')

#for pos, comida in enumerate(lanche):
#   print(f'Eu vou comer {comida} na posição {pos}')

# print(sorted(lanche))
# print(lanche)

a = (2, 5, 4)
b = (5, 4, 1)
c = a + b
print(c) # output: (2, 4, 5, 5, 4, 1)

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('Comida pra caramba!')