from src.manipulate_table import ManipulateTable

class DropTable:
    def __init__(self, query):
        self.manipulator = ManipulateTable()
        self.query = query

    def drop(self):
        self.manipulator.execute(self.query)

# EXEMPLO DE USO
if __name__ == "__main__":
    query_drop = "DROP TABLE IF EXISTS USERS"
    drop_table = DropTable(query_drop)
    drop_table.drop()