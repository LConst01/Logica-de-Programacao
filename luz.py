def estado_luz(estado):
    match estado:
        case "ligada":
            return "Luz ligada!"
        case "desligada":
            return "Luz desligadada!"
        case "piscando":
            return "Luz piscando!"
        case _:
            return "Opção inválida!"
status = input("Digite o estado da luz: ")

resultado = estado_luz(status)
print(resultado)