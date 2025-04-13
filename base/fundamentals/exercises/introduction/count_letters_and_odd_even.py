'''
Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.
'''
def check_chars(string):
    type = {'upper': 0, 'lower': 0}
    for char in string:
        if char.isupper():
            type['upper'] += 1
        elif char.islower():
            type['lower'] += 1
    
    print(f'Texto original: {string}')
    print(f'Número de letras maiúsculas: {type['upper']}')
    print(f'Número de letras minúsculas: {type['lower']}')

check_chars('Hello World!')

'''
Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.
'''
def check_numbers(numbers):
    even = []
    odd = []
    
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    
    print(f'Números pares: {even}')
    print(f'Números ímpares: {odd}')
    
check_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

