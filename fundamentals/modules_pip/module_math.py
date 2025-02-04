import math

# PI
print(math.pi)

# ACESSANDO NUMERO EULER
print(math.e)

# ARREDONDANDO APRA CIMA E PARA BAIXO
num = 10.4
print(math.ceil(num)) # CIMA
print(math.floor(num)) # BAIXO

# FATORIAL
factorial = int(input("Digite um numero: "))
print(math.factorial(factorial))

# POTENCIA
number = float(input("Digite um numero: "))
power = float(input("Digite apotencia: "))
print(math.pow(number, power))

# RAIZ QUADRADA
sqrt = float(input("Digite um numero e descubra a raiz: "))
print(f"{math.sqrt(sqrt):.2f}")

# MDC
mdc = math.gcd(25, 100)
print(mdc)

# LOG
print(math.log(10))