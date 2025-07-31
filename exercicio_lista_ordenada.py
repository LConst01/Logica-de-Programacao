def ordenar_lista(lista):
    if not lista:
        return[]

    lista_ordenada= sorted(lista)
    
    print(f"Lista ordenada: {lista_ordenada}")

lista1 = [10, 2, 5, 9, 1, 0]
ordenar_lista(lista1)