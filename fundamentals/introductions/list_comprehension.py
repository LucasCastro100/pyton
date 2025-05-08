# EXEMPLOS PARA ENTENDIMENTO
# LISTANDO DE 0 A 10 OS NUMEROS MENOR QUE 4 (SEM LIST COMPREHENSION)
for i in range(10):
    if i < 4 :
        print(i)
        
# LISTANDO DE 0 A 10 OS NUMEROS MENOR QUE 4 (COM LIST COMPREHENSION)
listComprehension =  ([i for i in range(10) if i < 4])
print(listComprehension)

filmesList = ['Star Wars', 'Indiana Jones', 'Harry Potter', 'Senhor dos Anéis']

# RECUPERANDO FILMES QUE TENHAM A LETRA A
newList = [x for x in filmesList if 'a' in x]
print(newList)

# RECUPERANDO FILMES QUE NÃO SEJAM HARRY POTTER
newFilmes = [x for x in filmesList if x != 'Harry Potter']
print(newFilmes)