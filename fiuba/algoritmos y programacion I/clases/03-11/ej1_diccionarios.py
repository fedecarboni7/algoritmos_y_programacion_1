#Programar una funcion que dada una palabra, calcula la cantidad de veces que está cada una de las letras que contiene

def cantidad_de_letras (palabra):
    cant_letras = {}
    for letra in palabra:
        if letra not in cant_letras:
            cant_letras[letra] = 1
        else:
            cant_letras[letra] += 1

    for letra in cant_letras:
        print("La letra", letra, " se encuentra", cant_letras[letra], " veces")

palabra = input("cargar palabra: ")
cantidad_de_letras(palabra)
