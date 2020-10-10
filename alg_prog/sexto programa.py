total_pares = 0
numero = int(input("Numero: "))
for par in range(2,numero+1,2):
    total_pares += par
print("Suma total de numeros pares entre 2 y",numero,"=",total_pares)
