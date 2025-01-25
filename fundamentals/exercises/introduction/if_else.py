'''
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,35 para viagens mais longas.
'''

distance = float(input('Digite a distância que deseja percorrer em km: '))

if distance <= 200:
    price = distance * 0.50
else:    
    price = distance * 0.35
    
print(f'O preço da passagem é R$ {price:.2f}')

'''
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
'''

salary = float(input('Digite o salário do funcionário: '))
increase = 0

if salary > 1250:
    increase = 10
else:
    increase = 15
    
new_salary = salary + (salary * increase / 100)
print(f'O novo salário é R$ {new_salary:.2f}')