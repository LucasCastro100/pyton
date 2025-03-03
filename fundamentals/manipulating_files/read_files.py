'''
Arquivos:

w - write (escrita)
r - read (leitura)
a - append (adicionar)
'''

with open("fundamentals/manipulating_files/dados/names.txt", "r", encoding="utf-8") as file:
    for line in file:
        # print(line) nesse formato ele retorna com espaço entre as linhas
        print(line.strip()) # com o strip ele remove o espaço entre as linhas    