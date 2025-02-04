'''
Escreva um programa em Python para verificar se uma string contém apenas um determinado conjunto de caracteres (neste caso, a-z, A-Z e 0-9).
'''

import re

'''
pattern = r'^[a-zA-Z0-9 ]+$' # assim valida tb o espaço
pattern = r'^[a-zA-Z0-9]+$' # assim o espaço não conta
'''

pattern = r'^[a-zA-Z0-9]+$'
phrase = "Lucas e um cara 10, porem as vezes a area de TI fez ele ficar louco!"

if re.match(pattern, phrase):
    print("A string contém apenas a-z, A-Z e 0-9.")
else:
    print("A string contém caracteres fora do conjunto permitido.")
    
# O REGEX SERVE PARA VALIDAR CARACTERES ENTAO TAMBEM PODEMOS RESOLVER ASSIM

def check_character(string):
    rule = re.compile(r'[^a-zA-Z0-9]') # AQUI PASSO VARIAS REGRAS PARA VALIDAR
    string = rule.search(string)
    return not bool(string)

print(check_character("ABCDEFabcdef123450")) 
print(check_character("*&%@#!}{"))