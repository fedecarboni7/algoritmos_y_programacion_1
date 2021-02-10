def leer_registro(fh):
    
    linea = fh.readline()
    
    if linea:
        registro = linea.rstrip('\n').split(',')
    else:
        registro = '99999','','',''
        
    return registro

def merge_inscripciones():
    ruta = "C:\\Users\\federico.carboni\\Desktop\\FIUBA Repo\\algoritmos y programacion I\\archivos (csv, txt, bin)\\ejercicio_inscripciones\\"

    inscr_web_fh     = open(f'{ruta}inscripciones_web.csv','r')
    inscr_tel_fh     = open(f'{ruta}inscripciones_tel.csv','r')
    inscr_pre_fh     = open(f'{ruta}inscripciones_pre.csv','r')
    inscripciones_fh = open(f'{ruta}inscripciones.csv','w')
    
    padron_web,materia_web,fecha_web,curso_web = leer_registro(inscr_web_fh)
    padron_tel,materia_tel,fecha_tel,curso_tel = leer_registro(inscr_tel_fh)
    padron_pre,materia_pre,fecha_pre,curso_pre = leer_registro(inscr_pre_fh)
    
    while padron_web != '99999' or padron_tel != '99999' or padron_pre != '99999':
        
        clave_web = padron_web + materia_web + fecha_web
        clave_tel = padron_tel + materia_tel + fecha_tel
        clave_pre = padron_pre + materia_pre + fecha_pre
        
        menor = min(clave_web,clave_tel,clave_pre)
        
        while padron_web != '99999' and clave_web == menor:
            
            inscripciones_fh.write('{},{},{},{}\n'.format(padron_web,materia_web,fecha_web,curso_web))
            
            padron_web,materia_web,fecha_web,curso_web = leer_registro(inscr_web_fh)
            
            clave_web = padron_web + materia_web + fecha_web
            
        while padron_tel != '99999' and clave_tel == menor:
            
            inscripciones_fh.write('{},{},{},{}\n'.format(padron_tel,materia_tel,fecha_tel,curso_tel))
            
            padron_tel,materia_tel,fecha_tel,curso_tel = leer_registro(inscr_tel_fh)
            
            clave_tel = padron_tel + materia_tel + fecha_tel
            
        while padron_pre != '99999' and clave_pre == menor:
            
            inscripciones_fh.write('{},{},{},{}\n'.format(padron_pre,materia_pre,fecha_pre,curso_pre))
            
            padron_pre,materia_pre,fecha_pre,curso_pre = leer_registro(inscr_pre_fh)
            
            clave_pre = padron_pre + materia_pre + fecha_pre
            
   
    inscr_web_fh.close()
    inscr_tel_fh.close()
    inscr_pre_fh.close()
    inscripciones_fh.close()
    
    return

merge_inscripciones()