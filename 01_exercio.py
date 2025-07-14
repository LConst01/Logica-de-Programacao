#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações


while True:
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite sua senha: ")
    
    if nome.lower == senha.lower:
        print(f"Senha não pode ser igual a nome!\n")
        continue
    if nome != senha:
        print(f"Cadastro Concluído")
        break


    
    

