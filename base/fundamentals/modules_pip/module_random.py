import random

# SELECIONA O VALOR ALEATORIO DE UMA LISTA
list1 = [15, 25, 36, 45, 78, 54, 89, 53, 15, 20]
print(random.choice(list1))

# GERA UM NUMERO ALEATORIO EM UM INTERVALO DE VALORES
r1 = random.randint(5, 15)
print(r1)

# SELECIONA CARACTERE ALEATORIO DE UMA STRING
name = "Lucas Oliveira"
r2 = random.choice(name)
print(r2)

# SELECIONA MAIS DE UM VALRO ALEATORIO
# sintaxe random.sample(sequencia, tamanho)
num_choices = 3
random_choices = random.sample(list1, num_choices)
print(random_choices)