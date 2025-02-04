import statistics

# MÉDIA
print(statistics.mean([5, 5, 15, 5, 10])) 

# MEDIANA
print(statistics.median([5, 5, 15, 5, 10]))

# MODA (PEGAR O NUMERO QUE MAIS SE REPETE)
print(statistics.mode([1, 5, 8, 7, 4, 5, 6, 9, 3, 2, 5, 4, 1, 5, 1, 4, 1, 2, 5, 4, 1, 7, 8, 9, 2]))

# DESVIO PADRÃO
"""
Medida de dispersão do conjunto, ou seja, uma medida 
que indica quão uniformes são os dados do conjunto.

- Quanto mais próximo de 0, significa que os dados
do conjunto estão menos dispersos
"""
print(statistics.stdev([1, 1.5, 2, 3.75, 8.78, 5, 6, 4, 9, 8.52, 4.58, 3.25, 7.48]))
