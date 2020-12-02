def leer_info(fh):
    linea = fh.readline()
    if linea:
        registro = linea.rstrip("\n").split(",")
    else:
        registro = ["999999","0"]
    return registro


movsbane= open("C:\\Users\\feden\\Documents\\Archivos\\UBA\\FIUBA\\Algoritmos y programacion I\\ejercicios\\moviBANE.txt", 'rt') 
movshb = open("C:\\Users\\feden\\Documents\\Archivos\\UBA\\FIUBA\\Algoritmos y programacion I\\ejercicios\\MoviHB.txt", 'rt') 
movssuc = open("C:\\Users\\feden\\Documents\\Archivos\\UBA\\FIUBA\\Algoritmos y programacion I\\ejercicios\\MoviSUC.txt", 'rt') 
max = '999999'
bane_cta, bane_importe = leer_info(movsbane)
hb_cta, hb_importe = leer_info(movshb)
suc_cta, suc_importe = leer_info(movssuc)
total = 0
while bane_cta != max or hb_cta != max or  suc_cta != max:
    tot_cta = 0
    men = min(hb_cta, bane_cta, suc_cta)  # min es una función de python
    print('cta:', men)
    while bane_cta == men and bane_cta!= max:
        tot_cta += int(bane_importe)
        bane_cta, bane_importe = leer_info(movsbane)
    while hb_cta == men and hb_cta!= max:
        tot_cta += int(hb_importe)
        hb_cta, hb_importe = leer_info(movshb)
    while suc_cta == men and suc_cta!= max:
        tot_cta += int(suc_importe)
        suc_cta, suc_importe = leer_info(movssuc)
    print('Total por cta:', tot_cta)
    total += tot_cta
print('Total Gral:', total)
movsbane.close()
movshb.close()
movssuc.close()


def banelco_cuenta(men,bane_cta,bane_importe,tot_cta,max):
    while bane_cta == men and bane_cta!= max:
        tot_cta += int(bane_importe)
        bane_cta, bane_importe = leer_info(movsbane)
    return tot_cta


def home_banking(men,hb_cta,hb_importe,tot_cta,max):
    while hb_cta == men and hb_cta!= max:
        tot_cta += int(hb_importe)
        hb_cta, hb_importe = leer_info(movshb)
    return tot_cta


def sucursal_cuenta(men,suc_cta,suc_importe,tot_cta,max):
    while suc_cta == men and suc_cta!= max:
        tot_cta += int(suc_importe)
        suc_cta, suc_importe = leer_info(movssuc)
    return tot_cta
    