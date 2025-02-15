class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary # quando colocamos __salary ele fica com atributo privado
        
    def show(self):
        print(f"Nome {self.name} - Salario {self.__salary}")
        