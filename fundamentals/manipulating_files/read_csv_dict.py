courses = []

with open("fundamentals/manipulating_files/dados/courses.csv", "r", encoding="utf-8") as file:
    for line in file:        
        language, category = map(str.strip, line.rstrip().split(",")) # language = row[0] e category = row[1] e aqui ja removo os espaços em branco em ambos
        course = {}
        course["language"] = language
        course["category"] = category
        courses.append(course)

for course in courses: # reverse=True para ordenar de forma decrescente, se não passar nada, ordena de forma crescente
    print(course)