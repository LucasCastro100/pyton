from src.manipulate_table import ManipulateTable

class InsertTable:
    def __init__(self, table, columns, values):
        self.manipulator = ManipulateTable()
        self.table = table
        self.columns = columns
        self.values = values

    def execute(self):        
        # Construa a query de inserção com placeholders para os valores
        placeholders = ", ".join(["%s"] * len(self.values))  # Cria placeholders (%s) para os valores
        query = f"INSERT INTO {self.table} ({', '.join(self.columns)}) VALUES ({placeholders})"  # Cria a query completa
        
        print(f"Query gerada: {query}")  # Imprime a query para depuração

        # Chama o método de execução no ManipulateTable com a query e os parâmetros
        self.manipulator.execute(query, self.values)
        print("Dados inseridos com sucesso!")
