valor = int(input("Valor: "))
if valor > 0:
    print("Numero Positivo")
elif valor < 0:
    print("Numero Negativo")
else:
    print("Numero Neutro")

print("Es Par" if (valor%2==0)else "Es impar")

"""
Otra forma
if(valor%2==0):
   print("Es Par")
else:
   print("Es Impar")
"""
