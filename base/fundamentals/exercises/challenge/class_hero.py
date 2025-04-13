'''
Crie uma classe Hero com os atributos name, power e strength. Crie um método action que retorne a seguinte string: "{name} possui {strength} de força e {power} de poder de luta.
'''

class Hero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.strength = strength
        
    def action(self):
        return f"{self.name} possui {self.strength} de força e {self.power} de poder de luta."

new_hero = Hero("Goku", 10000, 9000)
print(new_hero.action())