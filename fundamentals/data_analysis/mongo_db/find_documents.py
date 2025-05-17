from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient()
db = client['nobel']

# Access the collections
prizes = db['prizes']
laureates = db['laureates']

# Count documents for gender infomation
# print(db.laureates.count_documents({'gender': 'female'}))
# print(db.laureates.count_documents({'gender': 'male'}))

# Count documents for die country information
# print(db.laureates.count_documents({'diedCountry': 'Germany'}))

# Filter compost

filter_doc = {    
    'diedCountry' : 'France',
    'gender' : 'female',
}

filters = db.laureates.count_documents(filter_doc)
first_find = db.laureates.find_one(filter_doc)
print(first_find['prizes'][0]['motivation'])
