'''
CLASSE NORMAL SEM CONSTRUTOR
class Movie:
    name = ""
    yearLaunch = 0
    includePlan = False
    note = 0
    durationMinutes = 0
    
movie = Movie()
movie.name = "AC 2"
movie.yearLaunch = 20015
movie.includePlan = False
movie.note = 5.0
movie.durationMinutes = 240
'''

'''
CLASSE COM COSNTRUTOR
class Movie:
    def __init__(self, name, yearLaunch, includePlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includePlan = includePlan
        self.note = note
        self.durationMinutes = durationMinutes
        
    def __str__(self): # __str__ como se fosse apra corrigir o erro 
        return f "Filme: {self.name}"
    
    
    
movie = Movie("AC 2", 2015, False, 5.0, 240)
'''
    
class Movie:
    def __init__(self, name, yearLaunch, includePlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includePlan = includePlan
        self.note = note
        self.durationMinutes = durationMinutes
        
    def __str__(self):
        return f"Filme: {self.name}"
    
    def techinal_sheet(self):
        print("-- DADOS DO FILME --")
        print(f"NOME: {self.name}")
        print(f"ANO LANÇAMENTO: {self.yearLaunch}")
        print(f"INCLUSO NO PLANO: {self.includePlan}")
        print(f"NOTA: {self.note}")
        print(f"DURAÇÃO: {self.durationMinutes} minutos\n")
    
# PRIMEIRO FILME
movie = Movie("AC 2", 2015, False, 5.0, 240)
print(movie)

movie.techinal_sheet()