def es_primo(numero):
    condicion = False
    if(numero == 2):
        condicion = True
    elif(numero > 2):
        for i in range(2, numero):
            if (numero % i == 0):
                break
        if (i+1 == numero):
            condicion = True
    return condicion


def filtrar_primos(numeros, menor_numero):
    return [i for i in numeros if es_primo(i) and i > menor_numero]


def ordenar_por_longitud_de_tuplas(lista_tuplas):
    return sorted(lista_tuplas, key=lambda i: len(i), reverse=True)


def concatenar_primeros_elementos(lista):
    lista_nueva = []
    for i in lista:
        lista_nueva += i[:2]
    return lista_nueva

