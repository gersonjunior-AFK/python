maior = None
menor = None

while True:
    numero = int(input("Digite um número positivo (ou um número negativo para encerrar): "))

    if numero < 0:
        break

    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

print("Maior valor digitado:", maior)
print("Menor valor digitado:", menor)
