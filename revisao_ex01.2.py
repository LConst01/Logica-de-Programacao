
from datetime import datetime

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

ano_atual = datetime.now().year

ano_cem = ano_atual + (100 - idade)

print(f"Você terá 100 anos em {ano_cem}")
