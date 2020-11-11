def contar_caracteres(cadena, caracter_1, caracter_2):
    contador = 0
    for caracter in cadena:
        if caracter in (caracter_1 + caracter_2):
            contador += 1
    return contador