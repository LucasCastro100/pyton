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

# FUNÇÃO RECURSIVA
def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)

numberFactorial = factorial(inputNumber)
print(numberFactorial)