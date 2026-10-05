# ==========================================
# Exercício: Estrutura de decisão
# Arquivo: ativ6.py
# Objetivo: explicar a lógica do programa.
# ==========================================

b = input("Digite seu nome: ")
s = float(input("Digite seu salário: "))
a = int(input("Digite o tempo de serviço: "))

match s:
    case salario if salario <= 2000 and a <= 5:
        print(b,", o abono do seu salário é: R$",s * 0.50)

    case salario if salario <= 2000 and a > 5:
        print(b,", o abono do seu salário é: R$",s * 0.75)

    case salario if salario > 2000 and a <= 8:
        print(b,", o abono do seu salário é: R$",s * 0.60)

    case salario if salario > 2000 and a > 8:
        print(b,", o abono do seu salário é: R$",s * 0.90)