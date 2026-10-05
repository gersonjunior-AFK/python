# ==========================================
# Exercício: Estrutura de dados
# Arquivo: estrutura_de_dados.py
# Objetivo: mostrar como usar lista, dicionário e DataFrame.
# ==========================================

# 1) Criando uma lista com valores em ordem
lista = ["a", "b", "c", "d", "e"]

# 2) Acessando o primeiro elemento da lista
# Em Python, a primeira posição da lista começa em 0
print(lista[0])

# 3) Criando um dicionário com chaves e valores
# Cada chave representa uma identificação e cada valor é o dado associado
# Exemplo: "01" -> 10001
#          "02" -> 10002
#          "03" -> 10003
dic = {"01": 10001, "02": 10002, "03": 10003}

# 4) Acessando um valor do dicionário pela chave
# Quando usamos dic["01"], Python procura a chave "01" e mostra seu valor
print(dic["01"])

# 5) Importando a biblioteca pandas para trabalhar com tabelas
import pandas as pd

# 6) Criando um dicionário com listas de dados
# Cada chave vira uma coluna da tabela e cada lista vira uma coluna de valores
# Exemplo: a posição 0 de cada lista está relacionada com a mesma linha
# Ex: "arroz" -> quantidade 2300 -> preço 20.50
dados = {
    "produto": ["arroz", "feijao", "farinha", "sal"],
    "quantidade": [2300, 2900, 3000, 4000],
    "preco": [20.50, 18.90, 27.50, 12.50]
}

# 7) Transformando o dicionário em uma tabela (DataFrame)
df = pd.DataFrame(dados)

# 8) Exibindo a tabela no terminal
print(df)