nome_completo = input("Digite seu nome e sobrenome: ")

#versão original
print(nome_completo)

#Maiúsculas 
print(nome_completo.upper())

#Minúsculas
print(nome_completo.lower())

#Primeiro nome
nomes = nome_completo.split()
print(nomes[0]) #zero é referente ao primeiro nome / posição zero 

print(nomes[1])
