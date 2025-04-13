class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @classmethod
    def from_text(cls, string): # aqui  usamos o cls pq ele tem valor de referencia a classe
        import re 
        item = re.findall("é \w*", string)
        
        name = item[0][2:]
        price = item[1][2:]
        
        return cls(name, int(price))
    
wiiu = Console.from_text("Meu video game é WIIU e o preço é 1000 reais")
ps = Console.from_text("Meu video game é PS e o preço é 2000 reais")
xbox = Console.from_text("Meu video game é XBOX e o preço é 3000 reais")

print(wiiu.__dict__)
print(ps.__dict__)
print(xbox.__dict__)

#__dict__ trasnforma um objeto em dicionario