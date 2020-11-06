dicdesc = {}
descripciones = [(1, "Martillo"), (2, "Tornillo"), (5, "mechas")]
stock = {1: [2, 300], 2: [5000, 3], 5: [60, 400]}

for cod, desc in descripciones:
    dicdesc[cod] = desc
valor_inventario = 0
for codigo in stock:
    valor_prod = stock[codigo][0] * stock[codigo][1]
    valor_inventario += valor_prod
    print("El valor total del producto", dicdesc[codigo], "es", valor_prod)
print("El valor total del inventario es", valor_inventario)
