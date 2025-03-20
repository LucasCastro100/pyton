from src.manipulate_table import ManipulateTable

class DropTable:
    def __init__(self, query):
        self.manipulator = ManipulateTable()
        self.query = query

    def execute(self):
        self.manipulator.execute(self.query)