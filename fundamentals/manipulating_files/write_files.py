'''
Arquivos:

w - write (escrita)
r - read (leitura)
a - append (adicionar)
'''

name = input("Digite seu nome: ")

with open("fundamentals/manipulating_files/dados/names.txt", "w") as file:
    file.write(f"{name}\n")