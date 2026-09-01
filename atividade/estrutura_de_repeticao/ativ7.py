import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("Adivinhe o número secreto entre 1 e 100.")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")
        break
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print("Muito baixo! Tente novamente.")
