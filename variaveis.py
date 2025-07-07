aluno= "Lucca Cunha"  #string = caractere
ano= 2025 #int = inteiro
curso= "Técnico em Desenvolvimento de Sistemas" #string
matricula= True #Boolean


# prit sem fstring
print("Meu nome é " + aluno + ", estou matriculada no curso de " + curso + " no ano de " + str(ano) + ".")

# print com fstring
print(f"Meu nome é {aluno}, \nestou matriculado no curso de {curso}  \nno ano de {ano}.") #f de formatação
#\n pula linha