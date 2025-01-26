'''
Escreva um módulo em python para tratar algumas strings e que possua as seguintes funcionalidades:

Inverter uma string de trás pra frente.

Retornar apenas letras com índice par.

Retornar apenas letras com índice ímpar.
'''

import strings
inputString = input('Digite a palavra: ')

print(strings.inverse(inputString))
print(strings.even_char(inputString))
print(strings.odd_char(inputString))
