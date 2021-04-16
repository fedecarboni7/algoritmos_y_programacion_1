# Se tiene cargado en memoria un diccionario llamado Stock con clave Producto y valores cantidad y precio.
# Se pide calcular el valor total del inventario

stock = {1: [2, 300], 2: [5000, 3], 5: [60, 400]}
total = 0
for producto in stock:
    total += stock[producto][0] * stock[producto][1]
print(total)
