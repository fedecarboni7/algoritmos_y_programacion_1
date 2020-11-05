def insertar_separadores(cadena, separador, espaciado):
    cadena_final = cadena.split()
    for i in range(espaciado, len(cadena) + 1, espaciado):
        cadena_final.insert(i, separador)

    return print(str(cadena_final))

insertar_separadores("255255255255", ".", 3)