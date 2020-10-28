#Generar una lista que contenga ternas formadas por x, x^2, x^3 para x entre 1 y 5 .
lista = []
for i in range(1,6):
    lista += [[i,i**2,i**3]]
print(lista)
