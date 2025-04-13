from collections import Counter, namedtuple, deque
from operator import itemgetter

# CONTAR ITENS DE UMA LISTA
fruits = ["Maçã", "Banana", "Uva", "Pêra", "Uva","Maçã", "Laranja", "Abacaxi", "Tangerina", "Uva", "Pêra"]
print(fruits)
print(Counter(fruits))

# UTILIZANDO TUPLA NOMEADA
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game('Dragon Age', 245.50, 8.75)
print(g1)

# ORDENANDO DICIONARIOS
students = {"Rafael": 27, "Kathelin":27, "Lucas": 29, "Carlos":55, "Jane": 52}
a = sorted(students.items(), key=itemgetter(0))
print(students)
print(a)

# UTILIZANDO FILA AMBAS EXTREMIDADES | append (ADICIONA) - pop (REMOVE)
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
deq.append(60)
deq.popleft()
deq.pop()
print(deq)