peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 17:
    print("Situação: muito abaixo do peso")
elif imc > 17 and imc < 18.4:
    print("Situação: abaixo do peso")
elif imc > 18.5 and imc < 24.9:
    print("Situação: peso normal")
elif imc > 25 and imc < 29.9:
    print("Situação: sobrepeso")
elif imc > 30 and imc < 34.9:
    print("Situação: obesidade grau I")
elif imc > 35 and imc < 40:
    print("Situação: obesidade grau II")
else:
    print("Situação: obesidade grau III")
