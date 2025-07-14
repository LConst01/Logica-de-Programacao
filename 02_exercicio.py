while True:
    nome = input("Digite o nome do usuário: ")

    if len(nome) <= 2:
        print("Nome deve ter três caractéres ou mais!") 
    else:
        idade = int(input("Digite a sua idade: "))
        if idade > 150:
            print("Idade deve ser menor que 150!")
        else:
            salario = float(input("Digite o seu salário: "))
            if salario == 0:
                print("Salalário deve ser maior que zero!")
            else:
                generos = ['F', 'f', 'M', 'm', 'O', 'o']
                genero = input("Digite seu gênero. 'M' para msaculino, 'F' para feminino e  'O' para outro: ")
                if genero != generos:
                    print("Digite o gênero novamente!")
                else:
                    break
            
    
    