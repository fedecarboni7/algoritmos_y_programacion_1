resultado = 0
base = int(input("Ingrese la base: "))
potencia = int(input("Ingrese la potencia: "))
for i in range(0,potencia):
    resultado += base * base
print(resultado)