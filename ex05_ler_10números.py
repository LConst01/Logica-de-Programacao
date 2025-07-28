#ler 10 números e imprimir a soma, o maior e menor
numeros = []
def ler_numero():
    soma = 0
    maior = None
    menor = None # None: não tem nunhum valor definido / valor indefinido
    
    for i in range(10):
        num = float(input(f"Digite o {i+1}° número: "))
        
        
        soma += num
        
        if maior is None or num > maior:
            maior = num
            
        if menor is None or num < menor:
            menor = num
    print(f"A soma dos números é: {soma} ")
    print(f"O maior numero é: {maior}")
    print(f"o menor número é: {menor}")
ler_numero()