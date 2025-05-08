import random

# Gera um número aleatório entre 1 e 10
random_number = random.randint(1, 10)

while True:
    try:
        # Solicita ao usuário que digite um número de 1 a 10
        chose_number = int(input("Digite um número de 1 a 10 e veja se você vai acertar: "))
        break  # Sai do loop se a entrada for válida
    except ValueError:
        # Exibe uma mensagem de erro se a entrada não for um número inteiro válido
        print("Entrada inválida. Por favor, digite um número inteiro de 1 a 10.")

# Compara o número escolhido pelo usuário com o número aleatório gerado
if chose_number == random_number:
    print("Você acertou!")
else:
    print("Você errou!")
    

print(f'Número sorteado {random_number}')
print(f'Número escolhido {chose_number}')