def palabra_mas_larga(texto):
    palabra_larga = ""
    inicio_palabra = 0
    for i in range(0, len(texto)):
        if texto[i] == " ":
            palabra_actual = texto[inicio_palabra:i]
            if len(palabra_larga) < len(palabra_actual):
                palabra_larga = palabra_actual
            inicio_palabra = i + 1
    palabra_actual = texto[inicio_palabra:]
    if len(palabra_larga) < len(palabra_actual):
        palabra_larga = palabra_actual
    return palabra_larga
