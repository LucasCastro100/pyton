class Course:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail
        
    
    @staticmethod
    def courses_trail(trail): #aqui nao usamos o cls pq ele nao tem valor de referencia a classe
        if trail == "Python Fundamentos":
            courses = ['Dominando Python', 'Modulos e PIP', 'Orientação a Objeto']
        elif trail == "Automação com Python":
            courses = ['Automação de Tarefas', 'Web Scraping', 'Assistente Virtual']
        else:
            courses = ['A definir']
            
        return courses
            
print(Course.courses_trail('Python Fundamentos'))
print(Course.courses_trail('Automação com Python'))
print(Course.courses_trail(''))
        