def es_potencia_de_dos(numero):
    # tu codigo
    condicion = False
    for i in range(0, numero):
        if 2**i == numero:
            condicion = True
            break
    return condicion


''' prueba
numero = int(input("Ingresar numero: "))
print(es_potencia_de_dos(numero))'''
