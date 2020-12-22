import pickle

a_escritura = open("C:\\Users\\feden\\Documents\\Archivos\\UBA\\FIUBA\\Algoritmos y programacion I\\ejercicios\\test.txt",'wb')
numero = 2
pickle.dump(numero, a_escritura)
a_escritura.close()

a_lectura = open('C:\\Users\\feden\\Documents\\Archivos\\UBA\\FIUBA\\Algoritmos y programacion I\\ejercicios\\test.txt','rb')
x = pickle.load(a_lectura)
print(x)
y = x*5
print(y)