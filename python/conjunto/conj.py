conjuntoA = {"goiaba", "manga", "abacaxi", "laranja"}
conjuntoB = {"laranja", "abacaxi", "banana", "uva"}
print(conjuntoA.intersection(conjuntoB))  # Mostra os elementos que estão em ambos os conjuntos
print(conjuntoA & conjuntoB)  # Mostra os elementos que estão em ambos os conjuntos

print(conjuntoA.union(conjuntoB))  # Mostra todos os elementos de ambos os conjuntos, sem repetições
print(conjuntoA | conjuntoB)  # Mostra todos os elementos de ambos os conjuntos, sem repetições

print(conjuntoA.difference(conjuntoB))  # Mostra os elementos que estão em conjuntoA, mas não em conjuntoB
print(conjuntoA - conjuntoB)  # Mostra os elementos que estão em conjuntoA, mas não em conjuntoB