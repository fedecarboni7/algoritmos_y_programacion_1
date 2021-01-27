import pickle

a_escritura = open("C:\\Users\\federico.carboni\\Desktop\\FIUBA Repo\\algoritmos y programacion I\\archivos (csv, txt, bin)\\test.txt",'wb')
numero = 2
pickle.dump(numero, a_escritura)
a_escritura.close()

a_lectura = open('C:\\Users\\federico.carboni\\Desktop\\FIUBA Repo\\algoritmos y programacion I\\archivos (csv, txt, bin)\\test.txt','rb')
x = pickle.load(a_lectura)
print(x)
y = x*5
print(y)