i = 1 
while i <5: #equanto i menor que 5
    print(i)
    i += 1 # i = i + 1



i = 0 # i pode ser igual a "contador" / i = contador

while i < 4: 
    print("Olá!")
    i += 1
#While: Usa quando  quer repetir  o código ENQUANTO a condição for VERDADEIRA. Quando usar: quando não se conhece o número previamente
#For: quando se sabe o número de repetições ou quando interar sobre uma sequência



alunos = ["Fulana", "Beltrana", "Ciclana"]
for aluno in alunos: 
    print(f"Aluno: {aluno}")
 


frutas = ["Morango", "Abacate", "laranja"]
for fruta in frutas:
    print(f"Fruta: {fruta}")

#Tabuada
numero = int(input("Digite o número para ver a tabuada: "))
print(f"Tabuada do {numero}:")

for i in range (1,11): #range:sequência de números inteiros. range(início, parada)    
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")