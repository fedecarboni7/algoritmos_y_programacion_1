############################################################################
#
# Listar archivo elemento a elemento, separando cada uno de los datos
# que vienen en la línea e informando al final el total general de
# cantidad y de importe
#
########################### FUNCIONES ######################################
'''---------------------------------------------------------------------------
Funcion que hace el recorrido del archivo elemento a elemento, utilizando
un ciclo for. Dado que el archivo es un objeto iterable, no es necesario
utilizar en este caso una funcion de lectura, ya que el metodo de iteracion
se encarga de acceder a cada uno de los elementos (lineas), en el archivo.
Tambien como alternativa valida, se utiliza with open para la apertura.'''


def listar_archivo():
    with open('C:\\Users\\federico.carboni\\Desktop\\FIUBA Repo\\algoritmos y programacion I\\archivos (csv, txt, bin)\\ventas.csv', 'r') as arVentas:
        cant_total_gral = imp_total_gral = 0
        for linea in arVentas:
            cod_suc, cod_art, cant, imp = linea.rstrip("\n").split(",")
            print(cod_suc, cod_art, cant, imp)
            cant_total_gral += int(cant)
            imp_total_gral += float(imp)
        print("Total General: ", cant_total_gral, imp_total_gral)
    return


############################################################
listar_archivo()
