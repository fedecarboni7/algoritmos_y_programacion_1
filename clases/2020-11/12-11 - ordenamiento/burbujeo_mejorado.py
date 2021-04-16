def ordenarConBurbujeoMejorado(lista):
    ordenado = False
    longitud = len(lista) - 1
    i = 0
    while (i < longitud and not ordenado):
        ordenado = True
        for j in range(0, longitud - i):
            if lista[j] >= lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                ordenado = False
        i += 1
    return lista

print(ordenarConBurbujeoMejorado([1,2,1,4,2,56,3,6,8,3]))