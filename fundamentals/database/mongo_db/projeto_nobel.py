import requests
from pymongo import MongoClient

# 1 - Estabelece conexão com o MongoDB e database
client = MongoClient()

db = client['nobel']

# 2 - Ingestão dos Dados em Documentos
for collection_name in ["prizes", "laureates"]:
    response = requests.get(f'http://api.nobelprize.org/v1/{collection_name[:-1]}.json')
    documents = response.json()[collection_name]
    db[collection_name].insert_many(documents)
    
# 3 - Consulta de Documentos
prizes = db['prizes']
laureates = db['laureates']

len_prizes = prizes.count_documents({})
len_laureates = laureates.count_documents({})

print(len_prizes)
print(len_laureates)