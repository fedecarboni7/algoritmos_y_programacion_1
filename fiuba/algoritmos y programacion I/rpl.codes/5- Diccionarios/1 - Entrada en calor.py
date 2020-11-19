def numeros_al_cuadrado(numero):
    return {i: i**2 for i in range(1, numero+1)}


def mezclar_diccionarios(dicc_uno, dicc_dos):
    dicc_uno.update(dicc_dos)
    return dicc_uno


def filtrar_por_sumar_diez(diccionario):
    return {i: diccionario[i] for i in diccionario if i + diccionario[i] >= 10}


def ordenar_valores_por_longitud(diccionario):
    lista = [diccionario[i] for i in diccionario]
    return sorted(lista, key=lambda j: len(j), reverse=True)
