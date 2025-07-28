def dia_da_semana(numero):
    match numero:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda-feira"
        case 3:
            return "Terça-feira"
        case 4:
            return "Quarta-feira"
        case 5:
            return "Quinta-feira"
        case 6:
            return "Sexta-feira"
        case 7:
            return "Sábado"
        case _:
            return "Dia inválido!"           

entrada = int(input("Digite um número de 1 a 7 para dia da semana: "))

resultado = dia_da_semana(entrada)
print(resultado)