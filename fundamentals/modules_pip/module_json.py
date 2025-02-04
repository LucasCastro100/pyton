import json

# STRING PARA DICIONARIOS
person = '{"name": "Lucas", "languagens": ["Python", "PHP"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['name'])

# CONVERTENDO DICIONARIO PARA JSON 
person_json = json.dumps(person_dict)
print(person_json)

# FORMATANDO JSON   
print(json.dumps(person_dict, indent=4, sort_keys=True))

# SALVANDO JSON EM TXT - ESSE "W" SIGNIFICA APRA CRIAR O ARQUIVO
with open('person.txt', 'w') as json_file:
    json.dump(person_dict, json_file)

# LENDO JSON DE TXT
with open('person.txt', 'r') as json_file:
    person_dict = json.load(json_file)
    print(person_dict)
    print(person_dict['name'])
    
# LENDO JSON EXTERNO
with open("person.txt", 'r') as json_file:
    data = json.load(json_file)
    print(data['languagens'])