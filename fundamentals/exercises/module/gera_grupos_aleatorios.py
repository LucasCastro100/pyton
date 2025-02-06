import random

# Lista de nomes
names_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack", "Kathy", "Leo"]

# Dividir a lista em grupos de 6
group_size = 6
num_groups = len(names_list) // group_size

# Dicionário para armazenar os grupos
groups_dict = {}

for i in range(num_groups):
    # Selecionar 4 itens aleatórios do grupo atual
    random_choices = random.sample(names_list[:group_size], 4)
    
    # Adicionar os itens selecionados ao dicionário
    groups_dict[f'Group {i+1}'] = random_choices
    
    # Remover os itens selecionados da lista original
    for item in random_choices:
        names_list.remove(item)

print(groups_dict)