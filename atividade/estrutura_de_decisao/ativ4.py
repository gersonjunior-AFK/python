n1 = int(input("Digite seu salario: "))
gratificacao = n1 * 0.1 if n1 < 3000 else n1 * 0.07
match n1:
    case salario if salario < 3000:
        print("voce recebeu a gratificacao de 10%",gratificacao)
    case salario if salario >= 3000:
        print("voce recebeu a gratificacao de 7%",gratificacao)

#  n1 = int(input("Digite seu salario: "))
#  match n1:
#  case salario if salario < 3000:
#  gratificacao = salario * 0.10
#  print("Você recebeu uma gratificação de 10%:", gratificacao)
#  case salario if salario >= 3000:
#  gratificacao = salario * 0.07
#  print("Você recebeu uma gratificação de 7%:", gratificacao)