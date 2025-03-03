'''
Escreva um programa Python para ler as primeiras n linhas de um arquivo.

O nome do arquivo e a quantidade de linhas devem ser passadas via parâmetro na função.
'''

def file_read_from_line(file_name, n_lines):
    from itertools import islice # pega quantidade de linhas do arquivo
    
    with open(file_name, encoding="utf-8") as file:
        for line in islice(file, n_lines):
            print(line.strip())
            
def sorted_names_file(file_name):
    name = []
    
    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            name.append(line.strip())
            
    print(sorted(name))
            
file_read_from_line('fundamentals/exercises/manipulating_files/dados/names.txt', 10)
sorted_names_file('fundamentals/exercises/manipulating_files/dados/names.txt')