'''EJ 1 .Se cuenta con 3 archivos de texto con información de los movimientos de stock en sus 3 sucursales, 
que están  ordenados código de producto en los que se registra  el movimiento de los  productos con el 
siguiente formato:
fecha
codigo_producto
cantidad_ingresos
cantidad_ventas
Se pide:
1- generar un archivo con igual formato y orden  que los  anteriores  que contenga un resumen  de 
los registros de los 3 archivos de entrada por Código de producto, y ordenado por dicho código.)un registro 
por codigo)
2-Stock actual de cada producto (suponer que se comienza con  cero productos).'''

movimientos1 = open("C:\\Users\\feden\\Documents\\Archivos\\UBA\\FIUBA\\Algoritmos y programacion I\\ejercicios\\mov1.txt", 'rt')
movimientos2 = open("C:\\Users\\feden\\Documents\\Archivos\\UBA\\FIUBA\\Algoritmos y programacion I\\ejercicios\\mov2.txt", 'rt')
movimientos3 = open("C:\\Users\\feden\\Documents\\Archivos\\UBA\\FIUBA\\Algoritmos y programacion I\\ejercicios\\mov3.txt", 'rt')
movimientos_tot = open("C:\\Users\\feden\\Documents\\Archivos\\UBA\\FIUBA\\Algoritmos y programacion I\\ejercicios\\mov_totales.txt", 'r+')
max = "999999"

def leer_info(fh):
    
    linea = fh.readline()
    
    if linea:
        registro = linea.rstrip('\n').split(',')
    else:
        registro = ["999999", "0", "0"]  
        
    return registro

def while_variable(codigo,importe,ventas,movimientos, importe_tot, ventas_tot):
    while codigo == men and codigo != max:
        importe_tot += int(importe)
        ventas_tot += int(ventas)
        codigo, importe, ventas = leer_info(movimientos)
    return codigo, importe, ventas, importe_tot, ventas_tot

codigo1, importe1, ventas1 = leer_info(movimientos1)
codigo2, importe2, ventas2 = leer_info(movimientos2)
codigo3, importe3, ventas3 = leer_info(movimientos3)
total = 0
while codigo1 != max or codigo2 != max or  codigo3 != max:
    tot_cta =importe_tot = ventas_tot = 0
    movimientos_tot.seek(0,2)
    men = min(codigo1, codigo2, codigo3)  # min es una función de python
    
    codigo1, importe1, ventas1, importe_tot, ventas_tot = while_variable(codigo1,importe1,ventas1,movimientos1,importe_tot, ventas_tot)
    
    codigo2, importe2, ventas2, importe_tot, ventas_tot = while_variable(codigo2,importe2,ventas2,movimientos2,importe_tot, ventas_tot)
    
    codigo3, importe3, ventas3, importe_tot, ventas_tot = while_variable(codigo3,importe3,ventas3,movimientos3,importe_tot, ventas_tot)
    
    print('Codigo:', men, "importe", importe_tot, "ventas", ventas_tot, "stock", importe_tot-ventas_tot)
    
    movimientos_tot.write(str(men) + "," + str(importe_tot) + "," + str(ventas_tot) + "\n")

movimientos_tot.seek(0)
print(movimientos_tot.readlines())
movimientos1.close()
movimientos2.close()
movimientos3.close()
movimientos_tot.close()