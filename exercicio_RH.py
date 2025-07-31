
def analisa_salarios(*salarios):

    if not salarios:
        return "Nenhum salário fornecido"
    
#calcular media salarial
    media = sum(salarios) / len(salarios)
    
#identificar o menor e o maior salário
    menor = min(salarios)
    maior = max(salarios)

#salarios acima da media   
    for salario in salarios:
        if salario > media:
            media +=1   
    
    total_pago = sum(salarios)
            
    return {
        "media_salarial": media,
        "menor_salario": menor,
        "maior_salario": maior,
        "colaboradores_acima_da_media": media,
        "total_pago": total_pago
    }

print(analisa_salarios(1500,2500,2000,1550))