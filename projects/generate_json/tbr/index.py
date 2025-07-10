import os
import json
import random
import string
import copy

def generate_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

categories = [
    "baby", "kids1", "kids2", "middle1", "middle2", "high", "technic", "university"
]

# Templates diferentes para as modalidades conforme categoria
modalidades_baby = {
    "gl": {"nota": [], "total": 0, "comentario": ""}
}

modalidades_kids1 = {
    "gl": {"nota": [], "total": 0, "comentario": ""},
    "dp": {"nota": {"r1": [], "r2": [], "r3": []}, "total": 0, "comentario": ""}
}

modalidades_others = {
    "mc": {"nota": [], "total": 0, "comentario": ""},
    "om": {"nota": [], "total": 0, "comentario": ""},
    "te": {"nota": [], "total": 0, "comentario": ""},
    "dp": {"nota": {"r1": [], "r2": [], "r3": []}, "total": 0, "comentario": ""}
}

teams = []
for category in categories:
    for i in range(5):
        # Escolhe o template correto conforme a categoria
        if category == "baby":
            modalidades = copy.deepcopy(modalidades_baby)
        elif category == "kids1":
            modalidades = copy.deepcopy(modalidades_kids1)
        else:
            modalidades = copy.deepcopy(modalidades_others)

        teams.append({
            "id": generate_id(),
            "name": f"Equipe {category.capitalize()} {i + 1}",
            "category": category,
            "modalities": modalidades,
            "nota_total": 0
        })

event = {
    "id": generate_id(),
    "nome": "Interno Teresa Valse",
    "data": "2025-08-09",
    "equipes": teams,    
}

event_json = [event]

base_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(base_dir, 'tbr_data_generated.json')

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(event_json, f, ensure_ascii=False, indent=4)

print(f"Arquivo salvo em: {filename}")
