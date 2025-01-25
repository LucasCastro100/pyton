#FOR
filmes = ['Star Wars', 'Indiana Jones', 'Harry Potter', 'Senhor dos Anéis']

print("="*50)
#exemplo de um foreach em js, o termo filme seria o item do array
for filme in filmes:
    print(filme)

print("="*50)
# QUANDO A CONDIÇÃO FOR ATENDIDA, ENCERRAR O LOOP
for filme in filmes:
    if filme == 'Harry Potter':
        break
    
    print(filme)

print("="*50)
# QUANDO A CONDIÇÃO FOR ATENDIDA, CONTINUAR O LOOP
for filme in filmes:
    if filme == 'Harry Potter':
        continue
    
    print(filme)
    
# WHILE
number = 0

while (number != -1):
    print(number)
    # SE DIGITAR -1, O LOOP É ENCERRADO
    number = int(input("Digite um número: "))