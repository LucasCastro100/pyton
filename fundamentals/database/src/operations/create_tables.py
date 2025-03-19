from src.manipulate_table import ManipulateTable

class CreateTable:
    def __init__(self, query):
        self.manipulator = ManipulateTable()
        self.query = query

    def create(self):
        self.manipulator.execute(self.query)