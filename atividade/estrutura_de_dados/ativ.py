# ==========================================
# Exercício: Estrutura de dados
# Arquivo: ativ.py
# Objetivo: demonstrar união e interseção entre conjuntos.
# ==========================================
nomes1 = {"lolo", "mamai", "rita", "pedro", "ana", "jose", "carlos", "paula"}
nomes2 = {"artur", "joao", "maria", "pietro", "ama", "jose", "juju", "ffaula"}
uniao = nomes1.union(nomes2)
intersecao = nomes1.intersection(nomes2)
print(f"União: {nomes1} uniao {nomes2} e {uniao}")
print(f"nomes1: {nomes1}, Interseção: {nomes2} e {intersecao}")
