import os
import json
import random
import string

def generate_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

categories = [
    "baby", "kids1", "kids2", "middle1", "middle2", "high", "technic", "university"
]

modalidades_template = {
    "mc": {"nota": 0, "comentario": ""},
    "om": {"nota": 0, "comentario": ""},
    "te": {"nota": 0, "comentario": ""},
    "dp": {"nota": 0, "comentario": ""}
}

teams = []
for category in categories:
    for i in range(5):
        teams.append({
            "id": generate_id(),
            "name": f"Equipe {category.capitalize()} {i + 1}",
            "category": category,
            "modalities": modalidades_template.copy()
        })

event = {
    "id": generate_id(),
    "nome": "Interno Teresa Valse",
    "data": "2025-08-09",
    "equipes": teams
}

event_json = [event]

# Pega a pasta onde está o script index.py (dentro da pasta tbr)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho completo do arquivo JSON dentro da mesma pasta do script (tbr)
filename = os.path.join(base_dir, 'tbr_data_generated.json')

# Salva o arquivo lá
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(event_json, f, ensure_ascii=False, indent=4)

print(f"Arquivo salvo em: {filename}")
