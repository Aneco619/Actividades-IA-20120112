laberinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def heuristica(start, objetivo):
    return abs(start[0] - objetivo[0]) + abs(start[1] - objetivo[1])

movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def a_estrella_recursiva(laberinto, actual, objetivo, antecesores, g_score, visitados):
    if actual == objetivo:
        camino = []
        while actual:
            camino.append(actual)
            actual = antecesores[actual]
        return camino[::-1], visitados

    for movimiento in movimientos:
        nueva_posicion = (actual[0] + movimiento[0], actual[1] + movimiento[1])

        if nueva_posicion[0] < 0 or nueva_posicion[1] < 0 or nueva_posicion[0] >= len(laberinto) or nueva_posicion[1] >= len(laberinto[0]):
            continue

        if laberinto[nueva_posicion[0]][nueva_posicion[1]] == 1:
            continue

        nuevo_g_score = g_score[actual] + 1

        if nueva_posicion not in g_score or nuevo_g_score < g_score[nueva_posicion]:
            g_score[nueva_posicion] = nuevo_g_score
            antecesores[nueva_posicion] = actual
            visitados.add(nueva_posicion)
            camino_encontrado, visitados = a_estrella_recursiva(laberinto, nueva_posicion, objetivo, antecesores, g_score, visitados)
            if camino_encontrado:
                return camino_encontrado, visitados

    return None, visitados

punto_inicio = (1, 0)
punto_final = (7, 0)
antecesores = {punto_inicio: None}
g_score = {punto_inicio: 0}
visitados = set([punto_inicio])

resultado, visitados = a_estrella_recursiva(laberinto, punto_inicio, punto_final, antecesores, g_score, visitados)

if resultado:
    print("El camino encontrado es:", resultado)
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if (fila, columna) in visitados:
                print("V", end=" ")  # Mostrar celdas visitadas
            else:
                print(laberinto[fila][columna], end=" ")
        print()
else:
    print("No se encontró un camino válido.")