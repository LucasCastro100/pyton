fisrtName = 'Lucas'
lastName = 'Oliveira'

print('='*100)
# OPERADOR DE CONCATENAÇÃO
name = fisrtName + ' ' + lastName
print(name)

print('='*100)
# OPERADOR DE REPETIÇÃO
letter = 'OI'
print(f'{letter} ' * 10)

print('='*100)
# OPERADOR DE BUSCA DE STRING
text = 'Lucas é legal' 
print('legal' in text)
print('oi' in text)

print('='*100)
# OPERADOR DE SLICING
text = 'Ola mundo'
print(text[0:5]) # Pega os caracteres da posição 0 até a 5, o espaço é considerado um caractere
print(text[4:]) # Pega os caracteres da posição 4 até o final
print(text[:3]) # Pega os caracteres do início até a posição 3
print(text[0:8:2]) # Pega os caracteres da posição 0 até a 8 pulando de 2 em 2
print(text[::2]) # Pega todos os caracteres pulando de 2 em 2
print(text[:8:-1]) # Pega os caracteres do início até a posição 8 pulando de 1 em 1
print(text[::-1]) # Inverte a string
print(text[::-2]) # Inverte a string pulando de 2 em 2
print(text[8:0:-1]) # Pega os caracteres da posição 8 até a 0 pulando de 1 em 1
print(text[8::-1]) # Pega os caracteres da posição 8 até o início pulando de 1 em 1

print('='*100)
# OPERADOR DE COMPARAÇÃO
text = 'Lucas'
print(text == 'Lucas') # Compara se as strings são iguais
print(text != 'Lucas') # Compara se as strings são diferentes
print(text == 'lucas') # Compara se as strings são iguais, porém é case sensitive
print(text.lower() == 'lucas') # Compara se as strings são iguais, porém converte para minúsculo
print(text.upper() == 'LUCAS') # Compara se as strings são iguais, porém converte para maiúsculo
print(text.lower() == 'lucas'.lower()) # Compara se as strings são iguais, porém converte para minúsculo
print(text.lower() == 'lucas'.upper()) # Compara se as strings são iguais, porém converte para minúsculo
print(text.startswith('Lu')) # Verifica se a string começa com 'Lu'
print(text.endswith('cas')) # Verifica se a string termina com 'cas'

print('='*100)
# OPERADOR DE FORMATAÇÃO
text = 'Lucas'
print(f'Olá {text}') # Formata a string com f-string
print('Olá {}'.format(text)) # Formata a string com format
print('Olá %s' % text) # Formata a string com %s
print('Olá %s %s' % (text, 'Oliveira')) # Formata a string com %s
print('Olá {0} {1}'.format(text, 'Oliveira')) # Formata a string com format
print('Olá {1} {0}'.format(text, 'Oliveira')) # Formata a string com format
print('Olá {name} {last}'.format(name=text, last='Oliveira')) # Formata a string com format

print('='*100)
# OPERADOR DE DIVISÃO
text = 'Lucas Oliveira'
print(text.split()) # Divide a string em uma lista
print(text.split('a')) # Divide a string em uma lista separando pelo caractere 'a'
print(text.split('a', 2)) # Divide a string em uma lista separando pelo caractere 'a' e limitando a 1 ou mais divisões n pode ser qualquer numero

print('='*100)
# OPERADOR DE SUBSTITUIÇÃO
text = 'Lucas Oliveira'
print(text.replace('Lucas', 'João')) # Substitui a palavra 'Lucas' por 'João'
print(text.replace('Lucas', 'João').replace('Oliveira', 'Silva')) # Substitui a palavra 'Lucas' por 'João' e 'Oliveira' por 'Silva'

print('='*100)
# OPERADOR DE REMOÇÃO DE ESPAÇOS
text = ' Lucas Oliveira '
print(text.strip()) # Remove os espaços do início e do final da string
print(text.lstrip()) # Remove os espaços do início da string
print(text.rstrip()) # Remove os espaços do final da string

print('='*100)
# OPERADOR DE CONTAGEM DE CARACTERES
text = 'Lucas Oliveira'
print(len(text)) # Conta quantos caracteres tem na string
print(text.count('a')) # Conta quantas vezes o caractere 'a' aparece na string
print(text.count('a', 0, 5)) # Conta quantas vezes o caractere 'a' aparece na string do índice 0 ao 5