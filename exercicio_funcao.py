'''def numero_maior(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        print(f"O maior núemero é: {num1}")
    elif num2 > num1 and num2 >= num3:
        print(f"O maior número é: {num2}")
    else:
        print(f"O maior número é: {num3}")
numero_maior(5, 6, 7)'''

def maior(primeiro, *restantes):
    return max(primeiro, *restantes)

print(maior(10, 4, 7, 22, 13, 17))
print(maior(5,5,5))


        
        