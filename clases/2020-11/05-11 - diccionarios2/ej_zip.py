precios = {"banana": 50, "manzana": 28, "naranja": 15, "pera": 30}
stock = {"banana": 60, "manzana": 00, "naranja": 32, "pera": 15}
total = 0
for frutas in zip(precios, stock):
    total += precios[frutas[0]] * stock[frutas[0]]
    print(frutas[0], "valor total:", precios[frutas[0]] * stock[frutas[0]])
print("Monto final: ", total)
