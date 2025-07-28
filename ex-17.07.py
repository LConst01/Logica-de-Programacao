#Construa um programa que receba o nome e o preço de 5 medicamentos de uma drogaria (considere que o usuário informou cinco medicamentos distintos).
#O programa deve informar o nome e o preço do medicamento mais barato, bem como a média aritimética dos preços informados.

medicamentos = []
for i in range(5):
    remedio = input(f"Digite o {i+1}º medicamento: ")
    valor_string =float (input(f"Digite o {i+1}º valor: ")).replace(",", ".") #replace: substitui  a vírgula por ponto
    valor = float
    medicamentos.append({"nome": remedio, "preco": valor})

mais_barato = min(medicamentos, key=lambda x: x['preco'])
media = sum(remedio ["preco"] for remedio in medicamentos)/5

print(f"\n Medicamento mais barato: {mais_barato["nome"]} (R$) {mais_barato['preco']}")

#media aritmética dos preços
print(f"Média aritmética dos preços: R$ {media:.2f}")


#função anônima: função sem nome  ---> lambda
#lambda argumentos: exprssão
#argumentos x parâmetros-
#parâmetro = declarado na definição de uma função/método
#argumento = valor real que fornece ao chamar a função 


    

    
    