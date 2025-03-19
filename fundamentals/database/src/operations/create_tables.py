from src.manipulate_table import ManipulateTable

class CreateTable:
    def __init__(self, query):
        self.manipulator = ManipulateTable()
        self.query = query

    def create(self):
        self.manipulator.execute(self.query)

# EXEMPLO DE USO
if __name__ == "__main__":
    query_create = """
    CREATE TABLE IF NOT EXISTS clientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        email VARCHAR(100)
    )
    """
    create_table = CreateTable(query_create)
    create_table.create()