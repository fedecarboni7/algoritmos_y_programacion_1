def filtrar_pares(lista):
    lista_pares = []
    for n in lista:
        if n % 2 == 0:
            lista_pares.append(n)
    return lista_pares

def filtrar_primos(lista):
    lista_primos = []
    for numero in lista:
        if es_primo(numero):
            lista_primos.append(numero)
    return lista_primos

def es_primo(numero):
    # tu codigo
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

def sumar_elementos(lista):
    suma = 0
    for n in lista:
        suma += n
    return suma

def esta_ordenada(lista):
    for n in range(1, len(lista)):
        if lista[n] < lista[n-1]:
            return False
    return True


def producto_escalar(vector_1, vector_2):
    suma = 0
    for v1, v2 in (vector_1, vector_2):
        suma += v1 * v2
    return suma

print(producto_escalar([2,5,3], [4,6,7]))

def letras_en_palabra(letras, frase):
    pass
