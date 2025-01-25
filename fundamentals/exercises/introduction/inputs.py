'''
Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, utilizando operadores de atribuição.
'''

number = int(input('Digite um número: '))
print(f'O antecessor de {number} é {number - 1} e o sucessor é {number + 1}')


'''
Escreva um programa em Python que leia quatro números e calcule a média entre esses números
'''

numbers = [] # Lista que armazenará os números
average = 0 # Iniciando média 0

qtd = int(input('Digite a quantidade de números que deseja adicionar e saber sua média: \n'))

for i in range(qtd):
    number = int(input(f'Digite o {i + 1}º número: '))
    numbers.append(number)
    
    if i == 0:
        sum = number
    else:
        sum += number
        
average = sum / qtd

print(f'A média dos números {numbers} é {average}')