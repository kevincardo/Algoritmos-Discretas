def multiplicacion_latina(matriz_A, matriz_H1, n):
    nueva_matriz = [[set() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matriz_A[i][j] and matriz_H1[j][k]:
                    for camino in matriz_A[i][j]:
                        # k+1 es el nodo destino. Si no está en el camino, se agrega.
                        if k + 1 not in camino:
                            nuevo_camino = camino + (k + 1,)
                            nueva_matriz[i][k].add(nuevo_camino)
    return nueva_matriz

def algoritmo_kaufmann_malgranger(adj_matrix):
    n = len(adj_matrix)
    # Paso 1: Crear H^1
    h1 = [[set() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and adj_matrix[i][j] == 1:
                h1[i][j].add((i + 1, j + 1))
    
    # Paso 2 y 3: Iteración r hasta n-1
    h_r = h1
    for r in range(1, n - 1):
        h_r = multiplicacion_latina(h_r, h1, n)
    
    return h_r

def solicitar_matriz():
    print("--- Configuración de la Matriz de Adyacencia ---")
    try:
        n = int(input("Ingrese el número de nodos (n): "))
        if n < 2:
            print("El grafo debe tener al menos 2 nodos.")
            return None
        
        matriz = []
        print(f"\nIngrese las filas de la matriz (use ceros y unos separados por espacios).")
        print(f"Cada fila debe tener {n} elementos:")
        
        for i in range(n):
            while True:
                fila_str = input(f"Fila {i+1}: ").split()
                if len(fila_str) != n:
                    print(f"Error: La fila debe tener exactamente {n} números. Intente de nuevo.")
                    continue
                try:
                    fila = [int(x) for x in fila_str]
                    matriz.append(fila)
                    break
                except ValueError:
                    print("Error: Ingrese solo números enteros (0 o 1).")
        
        return matriz
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        return None

# --- Ejecución Principal ---
if __name__ == "__main__":
    mi_matriz = solicitar_matriz()
    
    if mi_matriz:
        print("\nProcesando algoritmo de Kaufmann y Malgranger...")
        resultado = algoritmo_kaufmann_malgranger(mi_matriz)
        
        print("\n--- Caminos Hamiltonianos Encontrados ---")
        encontrado = False
        for i, fila in enumerate(resultado):
            for j, caminos in enumerate(fila):
                for c in caminos:
                    encontrado = True
                    print(f"Camino: {' -> '.join(map(str, c))}")
        
        if not encontrado:
            print("No existen caminos hamiltonianos en este grafo.")



