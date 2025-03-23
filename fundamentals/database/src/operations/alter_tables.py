from src.manipulate_table import ManipulateTable

class AlterTable:
    def __init__(self, query):
        self.manipulator = ManipulateTable()
        self.query = query

    def execute(self):
        self.manipulator.execute(self.query)
        print("Tabela alterada com sucesso!")