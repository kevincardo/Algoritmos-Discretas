from Operaciones import *


def fleury() -> None:
    print("Algoritmo de fleury para hallar circuitos eulerianos, envie un grafo conexo y descubra su circuito")
    matriz_de_adyacencia, n = ingresar_matriz()
    s = calcular_S(matriz_de_adyacencia, n)
    conexo: bool = es_conexo(s, n)

    if not conexo:
        print("El grafo no es conexo asi que NO existiran circuitos eulerianos")
        return

    grafo_euleriano: bool = paridad_de_grados(matriz_de_adyacencia, n)

    if not grafo_euleriano:
        return

    print("EL circuito euleriano del grafo es: ")
    print(circuito_euleriano(matriz_de_adyacencia, n))



def paridad_de_grados(matriz_de_adyacencia, n: int) -> bool:
    for i in range(n):
        grado = sum(matriz_de_adyacencia[i])

        if grado % 2 != 0:
            print("EL grafo no tiene todos sus vertices con grado par asi que NO existiran circuitos eulerianos")
            return False

    return True


def dfs(matriz_de_adyacencia, vertice, visitados) -> None:
    visitados.add(vertice)

    for vecino in range(len(matriz_de_adyacencia)):
        if matriz_de_adyacencia[vertice][vecino] == 1 and vecino not in visitados:
            dfs(matriz_de_adyacencia, vecino, visitados)


def contar_alcanzables(matriz_de_adyacencia, inicio) -> None:
    visitados = set()

    dfs(matriz_de_adyacencia, inicio, visitados)

    return len(visitados)


def es_puente(matriz_de_adyacencia, u, v) -> bool:
    antes = contar_alcanzables(matriz_de_adyacencia, u)

    matriz_de_adyacencia[u][v] = 0
    matriz_de_adyacencia[v][u] = 0

    despues = contar_alcanzables(matriz_de_adyacencia, u)

    matriz_de_adyacencia[u][v] = 1
    matriz_de_adyacencia[v][u] = 1

    return despues < antes


def circuito_euleriano(matriz_de_adyacencia, n: int) -> list:
    circuito = []

    actual = 0

    while True:

        circuito.append(actual)

        vecinos = []

        for i in range(n):

            if matriz_de_adyacencia[actual][i] == 1:
                vecinos.append(i)

        # Si ya no quedan aristas
        if len(vecinos) == 0:
            break

        siguiente = None

        # Intentar tomar una arista que NO sea puente
        for vecino in vecinos:

            # Si es la única opción, usarla
            if len(vecinos) == 1:
                siguiente = vecino
                break

            # Si no es puente, usarla
            if not es_puente(matriz_de_adyacencia, actual, vecino):
                siguiente = vecino
                break

        # Borrar arista usada
        matriz_de_adyacencia[actual][siguiente] = 0
        matriz_de_adyacencia[siguiente][actual] = 0

        # Avanzar
        actual = siguiente

    return circuito


fleury()