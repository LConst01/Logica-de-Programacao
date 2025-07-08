#Acessar elementos 
vetor = ["a", "b", "c", 1, 2, 3]
primeiro = vetor[0] #a

#Fatiamento (slicing)
#Pega uma faixa de elementos
sub_vetor = vetor[1:4]
#print(sub_vetor)

#Adicionar elementos
vetor.append("d") #adiciona elemento ao final do vetor
#Então ficaria ["a", "b", "c", 1, 2, 3, "d"]

#Adiciona vários elementos de uma vez
vetor.extend([4,5])
#print(vetor)

#Remover elementos
vetor.remove("b")
#print(vetor)

#Remover elemento por índice(posição)
del vetor[2]
#print(vetor)

#Atualizar elementos
    #Atribui um novo valor para posição específica / substituindo 
vetor[0] = "LC"
#print (vetor)

#len (IMPORTANTE) = LENGTH
#mostra qunatos elementos tem no vetor
tamnho_vetor = len(vetor)
#print(vetor)
#print(tamnho_vetor)

#Ordenação
matriculas = [6, 8, 1, 3, 2]
matriculas.sort()
#print(matriculas)

#Cria nova lista ordenada
novo_vetor = sorted(matriculas)

#Interação : percorre os elementos
for estudante in matriculas:
    print(estudante)

#Dividir string em palavras
frase = "Python é muito bom!"
palavras = frase.split()
print(palavras)

#Juntar palavras em string
nova_frase = " ".join(palavras)
print(nova_frase)

#Operações matemáticas em vetores numéricos
vetor_numerico = [1,2,3,4]
for i in range(len(vetor_numerico)):
    vetor_numerico[i] *=2 #vetor_numerico[i] = vetor_numerico[2] *2
print(vetor_numerico)