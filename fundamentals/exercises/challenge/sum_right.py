'''
Crie um programa que leia um número e retorne a soma dos números à direita desse número. E adicione em um nova lista.
'''

qtd = int(input('Digite a quantidade de números que deseja adicionar: '))
numbers = []

for i in range(qtd):
    number = int(input(f'Digite o {i+1}º número: '))
    numbers.append(number)

def sum_right(values):
    new_numbers = []
    
    for i in range(len(values)):
        sum_right = sum(values[i+1:])
        new_numbers.append(sum_right)
        
    return new_numbers

result = sum_right(numbers)
print(f"A nova lista com a soma dos números à direita é: {result}")