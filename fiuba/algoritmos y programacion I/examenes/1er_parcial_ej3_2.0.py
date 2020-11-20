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
tiempos["Grosjean"] = [6130, 115, 52]

puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
vuelta_mas_rapida = 1


def abandonaron(tiempos):
    cant_pilotos_abandonan = 0
    for piloto in tiempos:
        if tiempos[piloto][2] < 52:
            cant_pilotos_abandonan += 1
    return cant_pilotos_abandonan >= 3


def lista_ordenada(tiempos, puntos, vuelta_mas_rapida):
    lista = []
    tiempo_vuelta_min = 1000
    for piloto in tiempos:
        if tiempos[piloto][2] == 52:
            lista += [[piloto, tiempos[piloto][0]]]
    lista.sort(key=lambda i: i[1], reverse=False)
    lista = lista[0:10]
    for piloto in tiempos:
        if tiempos[piloto][1] < tiempo_vuelta_min:
            tiempo_vuelta_min = tiempos[piloto][1]
            tiempo_total_piloto = tiempos[piloto][0]
            piloto_vuelta_mas_rapida = piloto
    if [piloto_vuelta_mas_rapida, tiempo_total_piloto] not in lista:
        lista += [[piloto_vuelta_mas_rapida, vuelta_mas_rapida]]
    for i in range(0, len(puntos)):
        lista[i][1] = puntos[i]
        if lista[i][0] == piloto_vuelta_mas_rapida:
            lista[i][1] += vuelta_mas_rapida
    return lista

def main():
    print(abandonaron(tiempos))
    print(lista_ordenada(tiempos, puntos, vuelta_mas_rapida))

main()
