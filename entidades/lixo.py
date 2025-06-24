import random

TIPOS_LIXO = [
    ("Garrafa PET", "plastico"),
    ("Folha de papel", "papel"),
    ("Cascas de frutas", "organico"), 
    ("Pote de vidro", "vidro"),
    ("Lata de refrigerante", "metal"),
]

def gerar_lixo():
    return random.choice(TIPOS_LIXO)