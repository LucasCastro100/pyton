name = []

with open('fundamentals/manipulating_files/dados/names.txt', 'r') as file:
    for line in file:
        name.append(line.strip())
        
        
print(sorted(name))