def ingresar_matriz():
    #Pide al usuario el tamaño n y los valores de la matriz de adyacencia.

    n = int(input("¿Cuántos vértices tiene el grafo? n = "))
 
    print(f"\nIngresa la matriz de adyacencia ({n}x{n}).")
    print("Usa 1 si hay arista entre los vértices, 0 si no.\n")
 
    A = []
    for i in range(n):
        fila = []
        for j in range(n):
            valor = int(input(f"  A[{i}][{j}] = "))
            fila.append(valor)
        A.append(fila)
 
    return A, n
 
 
def multiplicar_matrices(A, B, n):

    #Multiplica dos matrices A y B de tamaño n×n.
    #Necesaria para calcular las potencias A^2, A^3, etc. 
    #Fórmula: C[i][j] = suma de A[i][k] * B[k][j]  para k en 0..n-1

    # Crear matriz resultado llena de ceros
    C = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0)
        C.append(fila)
 
    # Calcular cada posición de C
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
 
    return C
 
 
def calcular_S(A, n):
    
    #Calcula S = A^0 + A^1 + A^2 + ... + A^(n-1)
    #sumando posición a posición en cada paso.
 
    #A^0 = I (identidad: 1 en la diagonal, 0 en el resto)
    #A^k = A^(k-1) * A  (cada potencia se obtiene multiplicando la anterior por A)
    #S[i][j] acumula el total de todos los pasos
 
    # --- Inicializar S en ceros ---
    S = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0)
        S.append(fila)
 
    # Ak empieza como A^0 = identidad 
    Ak = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(1)   # diagonal principal = 1
            else:
                fila.append(0)
        Ak.append(fila)
 
    # Sumatoria: k va de 0 hasta n-1 
    for k in range(n):
        # Sumar Ak a S posición a posición
        for i in range(n):
            for j in range(n):
                S[i][j] += Ak[i][j]   # acumula en cada posición
 
        # Calcular la siguiente potencia: Ak = Ak * A
        Ak = multiplicar_matrices(Ak, A, n)
 
    return S
 
 
def es_conexo(S, n):
    #Revisa que TODAS las posiciones de S sean > 0.
    #Si encuentra algún cero, el grafo NO es conexo.

    for i in range(n):
        for j in range(n):
            if S[i][j] == 0:       
                return False       
    return True                    
 
 
# ── FUNCIÓN AUXILIAR: imprimir matriz ────────
def imprimir_matriz(M, nombre):
    print(f"\n  Matriz {nombre}:")
    for fila in M:
        print("   ", fila)


def main() -> None:
    matriz, n = ingresar_matriz()
    s = calcular_S(matriz, n)
    print(es_conexo(s, n))


if __name__ == "__main__":
    main()
