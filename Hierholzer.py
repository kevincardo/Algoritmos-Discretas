import random

def leer_grafo():
    # ingresar aristas una por una
    grafo = {}
    print("--- ENTRADA DE DATOS (TALLER DE DISCRETAS) ---")
    print("Ingresa las aristas como: origen destino (ej: 0 1)")
    print("Escribe 'fin' para terminar de ingresar.")
    
    while True:
        entrada = input(">> ").strip().lower()
        if entrada == 'fin':
            break
        
        try:
            # Convertimos la entrada tipo "0 1" en dos enteros independientes
            u, v = map(int, entrada.split())
            
            # Inicializamos las listas en el diccionario 
            if u not in grafo: grafo[u] = []
            if v not in grafo: grafo[v] = []
            
            # Añadimos la conexion en ambos sentidos por que es grafo no dirigido
            grafo[u].append(v)
            grafo[v].append(u)
        except ValueError:
            print("Error: Ingresa dos números separados por un espacio.")
            
    return grafo

def validar_grados_pares(grafo):
    #Verifica si todos los nodos tienen grado par.
    nodos_impares = []
    for nodo, vecinos in grafo.items():
        if len(vecinos) % 2 != 0:
            nodos_impares.append(nodo)
    
    if len(nodos_impares) > 0:
        print(f"\n ERROR: El grafo no es Euleriano.")
        print(f"Los nodos {nodos_impares} tienen grado impar.")
        return False
    
    print("\n VALIDACIÓN: Todos los nodos tienen grado par. Procediendo...")
    return True

def buscar_ciclo(grafo, inicio):
    """Construye un ciclo eliminando aristas (Paso 1, 3 y 4)."""
    ciclo = [inicio]
    actual = inicio
    
    while grafo[actual]: # Mientras el nodo actual tenga aristas
        proximo = grafo[actual].pop(0) # Paso 3: Olvidamos la arista
        grafo[proximo].remove(actual)  # La borramos también del vecino
        
        ciclo.append(proximo)
        actual = proximo
        
        if actual == inicio: # Ciclo cerrado
            break
    return ciclo

def hierholzer(grafo_original):
    #Algoritmo principal siguiendo los 6 pasos.
    # Copia para no dañar el original
    grafo = {u: list(v) for u, v in grafo_original.items()}
    
    # Paso 1: Seleccionar v0 y construir ciclo inicial C
    v0 = random.choice(list(grafo.keys()))
    C = buscar_ciclo(grafo, v0)

    # Paso 2 y 6: Repetir mientras queden aristas
    while any(len(v) > 0 for v in grafo.values()):
        
        # Paso 4: Buscar primer vértice en C con grado > 0
        for i, v_actual in enumerate(C):
            if len(grafo[v_actual]) > 0:
                # Construir ciclo C'
                C_prime = buscar_ciclo(grafo, v_actual)
                
                # Paso 5: Insertar C' en C
                C = C[:i] + C_prime + C[i+1:]
                break
                
    return C

# --- FLUJO PRINCIPAL ---
def main():
    # 1. Leer datos
    mi_grafo = leer_grafo()
    
    if not mi_grafo:
        print("Grafo vacío.")
        return

    # 2. Validar grados (Condición necesaria para circuito Euleriano)
    if validar_grados_pares(mi_grafo):
        # 3. Ejecutar algoritmo
        resultado = hierholzer(mi_grafo)
        print(f"\n🚀 CIRCUITO EULERIANO ENCONTRADO:")
        print(" -> ".join(map(str, resultado)))

if __name__ == "__main__":
    main()