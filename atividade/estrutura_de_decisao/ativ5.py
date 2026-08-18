peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 17:
    print("Situação: muito abaixo do peso")
elif imc < 18.5:
    print("Situação: abaixo do peso")
elif imc < 25:
    print("Situação: peso normal")
elif imc < 30:
    print("Situação: sobrepeso")
elif imc < 35:
    print("Situação: obesidade grau I")
elif imc < 40:
    print("Situação: obesidade grau II")
else:
    print("Situação: obesidade grau III")
