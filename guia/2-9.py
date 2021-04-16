segundos = int(input("Ingresar segundos:"))
dias = segundos // 86400
horas = (segundos // 3600) - (dias*24)
minutos = (segundos // 60) - (dias*1440) - (horas*60)
seg = segundos - (dias * 86400) - (horas * 3600) - (minutos * 60)

print(dias,"dias",horas,"horas",minutos,"minutos",seg,"segundos")
