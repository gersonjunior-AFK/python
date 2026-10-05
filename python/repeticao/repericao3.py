# ==========================================
# Exercício: Repetição em Python
# Arquivo: repericao3.py
# Objetivo: explicar a lógica do programa.
# ==========================================

mat =[
    ["ana","maria","joana"],
    ["carla","julia","marcela"],
    ["paula","renata","sandra"],
    ["adriana","aline","aline"]
]
for linha in range(4):
    for coluna in range(3):
        print(f"{mat[linha][coluna]}")