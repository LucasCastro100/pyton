# FUNÇÃO SEM ARGUMENTO (PARAMETRO)
def getNumber():
    return 42

number = getNumber()
print(number)

# FUNÇÃO COM ARGUMENTO (PARAMETRO)
def getNewNumber(number):
    return number

inputNumber = int(input('Digite um número: '))
newNumber = getNewNumber(inputNumber)
print(newNumber)

# FUNÇÃO RECURSIVA (CHAMA ELA MESMA)
def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)

numberFactorial = factorial(inputNumber)
print(numberFactorial)

# FUNCÃO ARGS (POSSO PASSAR QUANTOS ARGUEMTNOS EU QUISER, ARGUMENTOS PASSADOS COMO TUPLA)
def getNumbers(*args):
    return args

numbers = getNumbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers)

# FUNÇÃO KWARGS (POSSO PASSAR ARGUMENTOS COMO CHAVE E VALOR SEM PRECISAR DE DICIONARIO, ARGUMENTOS PASSADOS COMO DICIONARIO)
def presentations(**data):
    for key, value in data.items():
        print(f'{key} is {value}')
        
presentations(name='John', age=42, city='New York')

# FUNÇÃO LAMBDA (FUNÇÃO ANONIMA)
power = lambda number: number ** 2 # FUNÇÃO LAMBDA PARA ELEVAR UM NÚMERO AO QUADRADO

pair = lambda number: number % 2 == 0 # FUNÇÃO LAMBDA PARA VERIFICAR SE UM NÚMERO É PAR

sum = lambda number1, number2: number1 + number2 # FUNÇÃO LAMBDA PARA SOMAR DOIS NÚMEROS

reverse = lambda string: string[::-1] # FUNÇÃO LAMBDA PARA INVERTER UMA STRING

print(power(8))
print(pair(8))
print(sum(8, 15))
print(reverse('Hello World!'))