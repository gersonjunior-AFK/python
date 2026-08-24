s = float(input("digite seu salario: "))
match s:
    case salario if salario < 2500:
        print("voce esta isento de imposto de renda")
    case salario if salario >= 2500 and salario < 5000:
        print("voce pagara o imposto de renda")
        