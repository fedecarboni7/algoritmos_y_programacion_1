valor = 0
start = input("Ingresar movimientos? ")
while (start == "si"):
    valor += int(input("Ingrese movimiento:"))
    start = input("Desea continuar? ")
print(valor)