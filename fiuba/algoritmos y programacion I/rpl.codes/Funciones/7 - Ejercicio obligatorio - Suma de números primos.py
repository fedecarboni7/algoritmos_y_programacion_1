def suma_de_numeros_primos(numero):
    suma = 0
    for i in range(1, numero + 1):
        if es_primo(i):
            suma += i
    return suma


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
