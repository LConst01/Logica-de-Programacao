def maior():
    num = float(input("Digite o primeiro número: "))
    ndois = float(input("Digite o segundo número: "))
    ntres = float(input("Digite o segundo núemro: "))
    if num >= ndois and  num >= ntres:
        print(f"{num:.2f} é o maior número!")
    elif ndois >= num and ndois >= ntres:
        print(f"{ndois:.2f} é o maior núemro!")
    else:
        print(f"{ntres:.2f} é o maior número!")
maior()

