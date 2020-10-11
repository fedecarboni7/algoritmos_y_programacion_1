hora_partida = int(input("Ingresar hora de partida (24hs):"))
min_partida = int(input("Ingresar minutos de partida:"))
seg_partida = int(input("Ingresar segundos de partida:"))
hora_llegada = int(input("Ingresar hora de llegada:"))
min_llegada = int(input("Ingresar minutos de llegada:"))
seg_llegada = int(input("Ingresar segundos de llegada:"))
dist = float(input("Ingresar distancia recorrida (km):"))

partida = hora_partida + (min_partida/60) + (seg_partida/3600)
llegada = hora_llegada + (min_partida/60) + (seg_llegada/3600)
if llegada < partida:
    time = (llegada + 24) - partida
else:
    time = llegada - partida
vel = dist / time
print("Velocidad promedio:", vel, "km/h")