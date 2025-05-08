'''
Desenvolva novas funcionalidades para complementar o nosso gerenciamento da classe Filmes. Segue o escopo das funcionalidades:

Uma das funcionalidades requeridas é que o usuário possa realizar a avaliação de um filme passando uma nota com parâmetro e que essa nota seja salva no atributo específico da classe.

Assim que uma avaliação for realizada, deve ser incrementado o total de avaliadores daquele filme. Obs: Considere criar um atributo específico para esse fim.

Para cada filme ter uma nota de avaliação média que consiste na divisão do total de avaliação pelo total de avaliadores.
'''

class Movie:
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0

    def __str__(self):
        return f"Filme: {self.name}"
    
    def technical_sheet(self):
        print("####Dados do Filme####")
        print(f"Nome Filme: {self.name}")
        print(f"Ano Lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includedPlan}")
        print(f"Avaliação Filme: {self.totalEvaluation}")
        print(f"Total Avaliadores: {self.evaluators}")
        print(f"Duração Filme: {self.durationMinutes}")
        
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(f"Média do filme {self.name} é: {self.totalEvaluation / self.evaluators}") 
    
        
movie= Movie("Super Mario", 2023, False, 120)
movie.evaluate(8.5)
movie.evaluate(9.0)
movie.average()
movie.technical_sheet()

movie2 = Movie("Sonic", 2022, False, 110)
movie2.evaluate(10.0)
movie2.evaluate(9.5)
movie2.average()
movie2.technical_sheet()

    
