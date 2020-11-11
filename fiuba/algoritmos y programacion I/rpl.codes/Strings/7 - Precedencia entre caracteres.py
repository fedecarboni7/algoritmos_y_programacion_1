def precendencia_de_caracteres(cadena, caracter_1, caracter_2):
    subcadena = caracter_1 + caracter_2
    contador = 0
    for i in range(0, len(cadena)-1):
        if cadena[i:i+2] == subcadena:
            contador += 1
    return contador
