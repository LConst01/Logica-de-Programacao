def classificar_nota(nota):
    if not nota:
        return[]
    
    if nota >= 7:
        print("Você foi aprovado") 
    
    if nota >= 5: 
        print ("Você está de recuperação")
    
    else:
        return ("Você foi reprovado")
nota = float(input("Digite a sua nota: "))


classificar_nota(nota) 