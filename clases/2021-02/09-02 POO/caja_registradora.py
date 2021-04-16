from time import sleep

class Calculadora:
    def sumar_precio(self, productos):
        acumulado = 0
        for p in productos:
            acumulado += p[1]
        return acumulado
    
class PagoConTarjeta:
    def pagar(self, monto):
        print("Pagando {}...".format(monto))
        sleep(3)
        print("Pago realizado.")

class CajaRegistradora:
    productos_de_compra = []
    calculadora = Calculadora()
    pago_con_tarjeta = PagoConTarjeta()

    def agregar_producto(self, producto):
        self.productos_de_compra.append(producto)
    
    def imprimir_ticket(self):
        for producto in self.productos_de_compra:
            print("Producto: {}. Valor: {}.".format(producto[0], producto[1]))
        precio_total = self.calculadora.sumar_precio(self.productos_de_compra)
        print("Precio total de la compra: {}".format(precio_total))
        return precio_total
    
    def finalizar_compra(self):
        precio_total = self.imprimir_ticket()
        self.pago_con_tarjeta.pagar(precio_total)
        self.productos_de_compra = []

caja_registradora = CajaRegistradora()

caja_registradora.agregar_producto(("Coca-Cola 2L", 200))
caja_registradora.agregar_producto(("Papas Lays", 100))
caja_registradora.agregar_producto(("Pochoclo", 100))

caja_registradora.finalizar_compra()

caja_registradora.agregar_producto(("Coca-Cola 2L", 200))
caja_registradora.agregar_producto(("Oreo", 50))

caja_registradora.finalizar_compra()