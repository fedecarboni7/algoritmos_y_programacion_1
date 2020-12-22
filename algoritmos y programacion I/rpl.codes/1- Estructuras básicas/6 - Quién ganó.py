# tu codigo
equipo_local = input("Ingrese equipo local: ")
goles_local = int(input("Ingrese goles equipo local: "))
equipo_visita = input("Ingrese equipo visitante: ")
goles_visita = int(input("Ingrese goles equipo visitante: "))
if goles_local > goles_visita:
    print(equipo_local)
elif goles_local < goles_visita:
    print(equipo_visita)
else:
    print("Empate")