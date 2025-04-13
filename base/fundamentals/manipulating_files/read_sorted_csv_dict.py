courses = []

with open("fundamentals/manipulating_files/dados/courses.csv", "r", encoding="utf-8") as file:
    for line in file:        
        language, category = map(str.strip, line.rstrip().split(",")) # language = row[0] e category = row[1] e aqui ja removo os espaços em branco em ambos
        course = {}
        course["language"] = language
        course["category"] = category
        courses.append(course)

#apenas com o sorted não e possivel ordenar dicionarios, então é preciso passar uma função para ordenar
def get_language(course):
    return course["language"]

def get_category(course):
    return course["category"]

#agora eu vou passar a função get_language para o parametro key, para que ele ordene a lista de acordo com a chave language
print("\n")
for course in sorted(courses, key=get_language):
    print(course)    
    
#agora eu vou passar a função get_category para o parametro key, para que ele ordene a lista de acordo com a chave category
print("\n")
for course in sorted(courses, key=get_category):
    print(course)
    
#agora vamos usar o lambda para fazer a mesma coisa que fizemos com as funções get_language e get_category
print("\n")
for course in sorted(courses, key=lambda course: course["language"]):
    print(course)
    
print("\n")
for course in sorted(courses, key=lambda course: course["category"]):
    print(course)
