def insertar_separadores(cadena, separador, espaciado):
    cadena_acumulada = ""
    i = espaciado
    while(i < len(cadena)):
        cadena_acumulada += (cadena[i-espaciado:i]) + separador
        i += espaciado
    return cadena_acumulada + cadena[i-espaciado:]
