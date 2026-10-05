# ==========================================
# Exercício: Estrutura de dados
# Arquivo: ativ2.py
# Objetivo: mostrar acesso a lista e dicionário.
# ==========================================

lista = ["a", "b", "c", "d", "e"]
print(lista[0])


dic = {"01":10001, "02":10002, "03":10003}
print(dic["01"])

dic2 = {"produto":["arroz", "feijao","farinha", "sal"]
        , "quantidade":[2300, 2900, 3000, 4000]
        ,"preco":[20.50, 18.90, 27.50, 12.50]
        }
print(dic2["produto"])