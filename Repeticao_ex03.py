#Desenvolva um programa em python que utilize WHILE para permitir o cadastro de um número indeterminado de funcionários. 
#O programa deve encerrar o caastro quando o usuário digitar 0 e, ao final, exibir a lista completa dos funcionários registrados.

funcionarios = []

while True:
    nome = input ("Digite o nome do funcionário (ou 0 para encerrar): ")
    if nome == "0":
        break #pararda
    funcionarios.append(nome)
    
    if nome == "":
        print("Precisa digitar um nome.")
        funcionarios.remove(nome)
#ou
'''
while True:
    nome = input ("Digite o nome do funcionário (ou 0 para encerrar): ")
    if nome == "0":
        break #pararda
    funcionarios.append(nome)
    if nome.strip() == ""
        print()
'''
        

print("\nLista de funconários cadastrados: ")
for i, funcionario in enumerate(funcionarios, 1): #enumerate: itera(iterar=repetir) sobre a sequência 
#enumerate(obje a ser percorrido, valor inicial do índice)
    print(f"{i}. {funcionario}")