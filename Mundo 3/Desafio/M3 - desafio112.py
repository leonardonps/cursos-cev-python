# Mundo 3 - Desafio 112
# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
# que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam
# monetários
import utilidadesCeV.dado
import utilidadesCeV.moeda

value = utilidadesCeV.dado.readCurrency("Type a price: R$")
utilidadesCeV.moeda.summary(value, 10, 10)
