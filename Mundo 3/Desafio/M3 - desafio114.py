# Mundo 3 - Desafio 114
# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

# Answer by https://stackoverflow.com/questions/1949318/checking-if-a-website-is-up-via-python

from urllib.request import Request, urlopen

req = Request('http://pudim.com.br/')

try:
    response = urlopen(req)
except:
    print('\33[31mThis website is not acessible.\33[m')
else:
    print('\33[32mThis website is acessible.\33[m')


