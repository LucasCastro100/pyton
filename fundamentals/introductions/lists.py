# NOME | SOBRENOME | DATA DE NASCIMENTO | ALTURA | PESO
user = ['Lucas', 'Oliveira', '12/12/1995', '1.75', '87']

print('='*100)
# BUSCA O PRIMEIRO ITEM DA LISTA
print(user[0])

print('='*100)
# BUSCA O ÚLTIMO ITEM DA LISTA
print(user[-1])

print('='*100)
# BUSCA O UM ITEM ALEATORIO DA LISTA
print(user[2]) #AQUI NO CASO ELE ESTARIA TRAZENDO A DATA DE NASCIMENTO
print(user[1:3]) #AQUI NO CASO ELE ESTARIA TRAZENDO O SOBRENOME E A DATA DE NASCIMENTO
print(user[2:]) #AQUI NO CASO ELE ESTARIA TRAZENDO A DATA DE NASCIMENTO, ALTURA E PESO
print(user[:3]) #AQUI NO CASO ELE ESTARIA TRAZENDO O NOME, SOBRENOME E DATA DE NASCIMENTO

type_languages = []

'''
# ADICIONANDO UM NOVO ITEM NA LISTA
type_languages.append('Python')

# ADICIONANDO VÁRIOS ITENS NA LISTA
type_languages.extend(['Python', 'JavaScript', 'Java'])
'''

qtd_languages = int(input('Quantas linguagens você deseja adicionar? '))
for i in range(qtd_languages):
    language = input('Digite a linguagem: ')
    type_languages.append(language)

type_languages.sort()
print('='*100)
print(type_languages)


'''
#TAMANHO DA LISTA
len(type_languages)

#REMOVENDO UM ITEM DA LISTA
type_languages.remove('Python')

#REMOVENDO UM ITEM DA LISTA PELO INDICE
type_languages.pop(0)

#REMOVENDO TODOS OS ITENS DA LISTA
type_languages.clear()

#DELETANDO A LISTA
del type_languages

#VERIFICANDO SE UM ITEM ESTÁ NA LISTA
if 'Python' in type_languages:
    print('Python está na lista')
    
#VERIFICANDO A QUANTIDADE DE VEZES QUE UM ITEM ESTÁ NA LISTA
print(type_languages.count('Python'))

#VERIFICANDO O INDICE DE UM ITEM NA LISTA
print(type_languages.index('Python'))

#COPIANDO UMA LISTA
new_list = type_languages.copy()

#ADICIONANDO UM ITEM EM UMA POSIÇÃO ESPECIFICA
type_languages.insert(0, 'Python')

#REVERTENDO A LISTA
type_languages.reverse()

#SOMANDO DUAS LISTAS
new_list = type_languages + ['Java', 'C#']

#REPETINDO UMA LISTA
new_list = type_languages * 2

ENUMERATE
retorna tanto o índice quanto o valor do item atual em cada iteração. Isso é útil quando você precisa de ambos, o índice e o valor, ao iterar.
'''