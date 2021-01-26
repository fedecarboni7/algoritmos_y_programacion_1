# Se tienen los archivos evaluaciones_web.csv evaluaciones_pre.csv 
# formato de registro: padron,materia,nota
# Los archivos están ordenados por padron y materia
# Se quiere generar un archivo promedios.csv con los promedios ordenado por padron y materia
#Registro del archivo promedios: padron,materia,promedio
# c:\users\inés\evaluaciones_web.csv
# 80295,70.10,7.5
# 80297,70.10,10
# 80297,70.50,5
# 80300,70.10,4
# 80300,70.10,10
# 80301,70.10,7
# 80307,70.10,8
# c:\users\inés\evaluaciones_pre.csv
# 80293,70.10,10
# 80297,70.70,7
# 80297,70.40,4.5
# 80300,70.10,8
# 80300,70.10,9
# ---------------------------------------------
# Resultado esperado
# 80293,70.10,10.0
# 80295,70.10,7.5
# 80297,70.10,10.0
# 80297,70.50,5.0
# 80297,70.70,7.0
# 80297,70.40,4.5
# 80300,70.10,7.75
# 80301,70.10,7.0
# 80307,70.10,8.0

def leer_registro(fh):
    linea = fh.readline()
    if linea:
        registro = linea.rstrip('\n').split(',')
    else:
        registro = '99999','99.99',''
    return registro

def generar_archivo_promedios():
    
    evaluaciones_web_fh = open('C:\\Users\\feden\\Documents\\Archivos\\UBA\\FIUBA\\Algoritmos y programacion I\\ejercicios\\evaluaciones_web.csv','r')
    evaluaciones_pre_fh = open('C:\\Users\\feden\\Documents\\Archivos\\UBA\\FIUBA\\Algoritmos y programacion I\\ejercicios\\evaluaciones_pre.csv','r')
    promedios_fh        = open('C:\\Users\\feden\\Documents\\Archivos\\UBA\\FIUBA\\Algoritmos y programacion I\\ejercicios\\promedios.csv','w')
    
    padron_web, materia_web, nota_web = leer_registro(evaluaciones_web_fh)
    padron_pre, materia_pre, nota_pre = leer_registro(evaluaciones_pre_fh)
    
    while padron_web != '99999' or padron_pre != '99999':
        
        clave_web = padron_web + materia_web
        clave_pre = padron_pre + materia_pre
        
        menor = min(clave_web,clave_pre)
        
        menor_total_notas = 0.0
        menor_cant_notas  = 0
        
        while padron_web != '99999' and clave_web == menor:
            
            menor_total_notas += float(nota_web)
            menor_cant_notas  += 1
            
            padron_web, materia_web, nota_web = leer_registro(evaluaciones_web_fh)
            
            clave_web = padron_web + materia_web
            
        while padron_pre != '99999' and clave_pre == menor:
            
            menor_total_notas += float(nota_pre)
            menor_cant_notas  += 1
            
            padron_pre, materia_pre, nota_pre = leer_registro(evaluaciones_pre_fh)
            
            clave_pre = padron_pre + materia_pre
        
        promedio = menor_total_notas / menor_cant_notas
        
        menor_padron  = menor[0:5]
        menor_materia = menor[5:10]
            
        promedios_fh.write('{},{},{}\n'.format(menor_padron,menor_materia,promedio))
    
    evaluaciones_web_fh.close()
    evaluaciones_pre_fh.close()
    promedios_fh.close()
    
    return

generar_archivo_promedios()