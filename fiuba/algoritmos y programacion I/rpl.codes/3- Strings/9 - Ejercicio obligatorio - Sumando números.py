def sumar_caracteres_numericos(cadena):
    suma = 0
    for numero in cadena:
        if numero.isnumeric():
            suma += int(numero)
    return suma
