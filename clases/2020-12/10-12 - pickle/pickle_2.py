import pickle

def generar_diccionario():
    empleados = {}
    empleados[125] = ["Juan Carlos", 60]
    empleados[131] = ["Mariela Fernandez", 50]
    empleados[125] = ["Martina Calvanaro", 55]
    return empleados

def cargar_archivo(empleados):
    a_escritura = open('C:\\Users\\federico.carboni\\Desktop\\FIUBA Repo\\algoritmos y programacion I\\archivos (csv, txt, bin)\\prueba.dat','wb')
    for legajo in empleados:
        pickle.dump(legajo, a_escritura)
        pickle.dump(empleados[legajo], a_escritura)
    pickle.dump(0, a_escritura)
    a_escritura.close()

def leer_archivo():
    a_lectura = open('C:\\Users\\federico.carboni\\Desktop\\FIUBA Repo\\algoritmos y programacion I\\archivos (csv, txt, bin)\\prueba.dat','rb')
    legajo = pickle.load(a_lectura)
    while (legajo != 0):
        print(legajo)
        datos = pickle.load(a_lectura)
        print(datos)
        legajo = pickle.load(a_lectura)
    a_lectura.close()

def main():
    empleados = generar_diccionario()
    cargar_archivo(empleados)
    leer_archivo()

main()