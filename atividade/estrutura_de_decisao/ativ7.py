salario = float(input("Digite seu salario: "))
cargo = input("Digite seu cargo: ")
if cargo == 1:
    grat = salario * 0.25
elif cargo == 2:
    grat = salario * 0.15
elif cargo == 3:
    grat = salario * 0.10
else:
    grat = 0

print("O valor da gratificação é: R$", grat)