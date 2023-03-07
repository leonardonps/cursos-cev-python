# Mundo 3 - Desafio 109
# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ouu não formatado pela função moeda(), desenvolvida no desafio 108.

import utilidadesCeV.moeda

value = float(input('Type the price: R$'))

print(f"The double of {moeda.currency(value)} is {moeda.double(value)}")
print(f"The half of {moeda.currency(value)} is {moeda.half(value)}")
print(f"{moeda.currency(value)} + 15% equals to {moeda.increase(value, 15)}")
print(f"{moeda.currency(value)} - 15% equals to {moeda.decrease(value, 15)}")