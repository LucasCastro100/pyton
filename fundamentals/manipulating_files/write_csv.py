import csv

languages = input("Informe o nome da linguagem que deseja aprender: ")
category = input("Informe a categoria que a linguagem se encaixa: ")

with open('fundamentals/manipulating_files/dados/courses.csv', 'a', encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator='\n') # lineterminator='\n' para evitar quebra de linha
    writer.writerow([languages, category])