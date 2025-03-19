from src.manipulate_table import ManipulateTable

class AlterTable:
    def __init__(self, query):
        self.manipulator = ManipulateTable()
        self.query = query

    def alter(self):
        self.manipulator.execute(self.query)

# EXEMPLO DE USO
if __name__ == "__main__":
    query_alter = "ALTER TABLE clientes ADD COLUMN telefone VARCHAR(20)"
    alter_table = AlterTable(query_alter)
    alter_table.alter()