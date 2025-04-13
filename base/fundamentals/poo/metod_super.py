'''
CASO QUIZESEMOS UTILIZAR POLIMORFISMO BASTA APLICAR EM CADA CLASE POIS POLIMORFISMO ELE REPETE NAS CLASES POREM COM VALORES DIFERENTES
'''

class Phone:
    def __init__(self, brand, model_name, price):
        self._brand = brand
        self._model_name = model_name
        self._price = price
        
    def __str__(self):
        return f"{self._brand} {self._model_name}"
    
    @staticmethod
    def make_a_call(phone_num):
        print(f"Ligando para {phone_num}")
    
class SmartPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        super().__init__(brand, model_name, price) #aqui estamos aproveitando os dados da classe pai
        
        self._ram  = ram
        self._internal_memory  = internal_memory
        self._back_camera = back_camera

phone_1 = Phone("Motorola", "G5", 2500)
phone_1.make_a_call(34991535839)
print(phone_1)
print(f"o valor do {phone_1._brand} {phone_1._model_name} é {phone_1._price}")

phone_2 = SmartPhone("Xiaomi", "MI-14", 6500, "12GB", "512GB", "128MP")
print(phone_2)