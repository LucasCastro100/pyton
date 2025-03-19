from src.manipulate_table import ManipulateTable

class AlterTable:
    def __init__(self, query):
        self.manipulator = ManipulateTable()
        self.query = query

    def alter(self):
        self.manipulator.execute(self.query)