numero = int(input("Numero:"))
while(numero<0) or (numero >= 1000):
    print("ERROR: Valor ingresado inválido, reingrese valor")
    numero = int(input("Numero:"))
print("Numero valido ingresado:", numero)
