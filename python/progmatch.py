m = int(input("Digite o mes 1 a 12: "))
if m == 1:
    print("Janeiro")
elif m == 2:
    print("Fevereiro")
elif m == 3:
    print("Março")
elif m == 4:
    print("Abril")
elif m == 5:
    print("Maio")
else:
    print("outro mes")

match m:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case _:
        print("outro mes")