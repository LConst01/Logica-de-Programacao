#Crie um programa que peça ao usuário para digitar seu nome e sua idade. Imprima uma mensagem endereçada a ele que digite em que ano
#ele completará 100 anos.

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
ano = 2025 

nascimento = ano - idade

cem_anos= nascimento + 100 

print(f"Você, {nome}. Terá cem anos no ano de: {cem_anos}!")

