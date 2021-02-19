tiempos = {}
tiempos["Hamilton"] = [6115, 113, 52]
tiempos["Bottas"] = [3610, 115, 30]
tiempos["Verstappen"] = [6111, 114, 52]
tiempos["Perez"] = [6150, 115, 52]
tiempos["Leclerc"] = [6153, 116, 52]
tiempos["Ricciardo"] = [6140, 116, 52]
tiempos["Sainz"] = [6141, 116, 52]
tiempos["Norris"] = [6160, 115, 52]
tiempos["Albon"] = [6165, 114, 52]
tiempos["Gasly"] = [6172, 112, 52]
tiempos["Stroll"] = [6175, 115, 52]
tiempos["Ocon"] = [6177, 114, 52]
tiempos["Vettel"] = [4720, 111, 40]
tiempos["Kvyat"] = [700, 119, 5]
tiempos["Hulkenberg"] = [6201, 118, 52]
tiempos["Raikkonen"] = [6133, 114, 52]
tiempos["Giovinazzi"] = [1205, 118, 10]
tiempos["Grosjean"] = [6130, 11, 52]

puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
vuelta_mas_rapida = 1
total_vueltas = 52


def termino_carrera(vueltas):
    return vueltas >= total_vueltas


def abandonaron(tiempos):
    cant_pilotos_abandonan = 0
    for piloto in tiempos:
        if not termino_carrera(tiempos[piloto][2]):
            cant_pilotos_abandonan += 1
    return cant_pilotos_abandonan >= 3


def encontrar_piloto_vuelta_mas_rapida(tiempos):
    pilotos = list(tiempos.items())
    piloto_vuelta_mas_rapida = pilotos[0]
    for piloto in pilotos:
        if piloto[1][1] < piloto_vuelta_mas_rapida[1][1]:
            piloto_vuelta_mas_rapida = piloto
    return piloto_vuelta_mas_rapida


def lista_ordenada_pilotos_top(tiempos, top):
    pilotos = list(dict(filter(lambda piloto: termino_carrera(piloto[1][2]), tiempos.items())).items())
    pilotos.sort(key=lambda tupla: tupla[1][0])
    return pilotos[0:top]


def calcular_puntaje(tiempos, puntos, vuelta_mas_rapida):
    pilotos = lista_ordenada_pilotos_top(tiempos, len(puntos))
    piloto_vuelta_mas_rapida = encontrar_piloto_vuelta_mas_rapida(tiempos)
    lista_puntajes = []
    cant_puntos = len(puntos) if len(puntos) >= len(pilotos) else len(pilotos)
    for i in range(0, cant_puntos):
        if pilotos[i] == piloto_vuelta_mas_rapida:
            lista_puntajes.append((pilotos[i][0],puntos[i] + vuelta_mas_rapida))
        else:
            lista_puntajes.append((pilotos[i][0], puntos[i]))
    if piloto_vuelta_mas_rapida not in pilotos:
        lista_puntajes.append((piloto_vuelta_mas_rapida[0], vuelta_mas_rapida))
    return lista_puntajes

def mostrar_puntaje(lista_puntajes):
    for puntaje in lista_puntajes:
        print(puntaje[0], puntaje[1])

def main():
    print(abandonaron(tiempos))
    mostrar_puntaje(calcular_puntaje(tiempos, puntos, vuelta_mas_rapida))


main()
