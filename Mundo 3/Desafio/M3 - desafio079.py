# Mundo 3 - Desafio 079
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []

while True:

    valor = int(input('Digite um valor para ser inserido na lista: '))

    if valor in valores:
        print('A lista já possui esse valor. Tente outro')
    else:
        valores.append(valor)
        resp = str(input('Deseja inserir mais um valor[s/n]? ')).strip().upper()[0]
        while resp not in 'SN':
            resp = str(input('Ooops... Opção inválida! Digite S para sim ou N Não: ')).strip().upper()[0]
        if resp == 'N':
            break

print(f'Valores da lista:', sorted(valores))