print("Soma de digitos de um número menor que 100!")

numero = int(input("Digite um numero menor que 100, que deseja somar seus digitos: "))
if numero >= 100:
    print("Numero maior que 100! Digite outro numero")
else:
    unidade_dezena = numero // 10 #divisão real 
    unidade_milhar = numero % 10
    resultado = unidade_dezena + unidade_milhar
    print(f"O resultado da soma de digitos é: {resultado}")