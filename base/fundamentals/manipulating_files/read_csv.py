with open("fundamentals/manipulating_files/dados/courses.csv", "r", encoding="utf-8") as file:
    for line in file:        
        language, category = map(str.strip, line.rstrip().split(",")) # language = row[0] e category = row[1] e aqui ja removo os espaços em branco em mabos
        print(f"{language} - {category}")               