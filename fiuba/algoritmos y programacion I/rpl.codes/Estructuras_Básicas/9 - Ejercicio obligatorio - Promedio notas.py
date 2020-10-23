# tu codigo
suma = 0
i = 0
nota = int(input("Ingrese nota o 0 para terminar: "))
while nota <= 10 and nota > 0:
    suma += nota
    i += 1
    nota = int(input("Ingrese nota o 0 para terminar: "))
print("El promedio es:",suma / i)