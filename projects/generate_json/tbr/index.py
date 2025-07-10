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

# Templates modalidades por categoria
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

# Modalidades possíveis no ranking do evento
default_modalities = ["ap", "mc", "om", "te", "dp"]

def random_modalities():
    # 30% chance de ser lista vazia (sem modalidades)
    if random.random() < 0.3:
        return []
    count = random.randint(1, len(default_modalities))
    return random.sample(default_modalities, count)

# Gera modalidades para o ranking do evento
modalities_to_show = random_modalities()

# Monta config do ranking do evento
ranking_config = {
    "modalities_to_show": modalities_to_show,
    "top_positions": 0 if len(modalities_to_show) == 0 else 1,
    "general_top_positions": random.randint(1, 3)
}

teams = []

# Gera equipes para todas categorias (em média 5 por categoria)
for category in categories:
    for i in range(5):
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
    "ranking_config": ranking_config,
    "equipes": teams  # sempre preenchido
}

event_json = [event]

base_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(base_dir, 'data-tbr.json')

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(event_json, f, ensure_ascii=False, indent=4)

print(f"Arquivo salvo em: {filename}")
print(f"Configuração do ranking no evento: {ranking_config}")
