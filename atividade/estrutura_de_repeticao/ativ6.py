pares = 0
impares = 0

while True:
    numero = int(input("Digite um número inteiro (-1 para encerrar): "))

    if numero == -1:
        break
    if numero == 0 or numero == 1:
        continue
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
