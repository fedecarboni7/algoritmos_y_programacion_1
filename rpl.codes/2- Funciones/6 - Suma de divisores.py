def suma_de_divisores(numero):
    # tu codigo
    suma = 0
    for i in range(2, numero):
        if(numero % i) == 0:
            suma += i
    return suma
