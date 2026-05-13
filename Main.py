from Operaciones import *

def main():
    print("=== VERIFICADOR DE CONEXIDAD DE GRAFOS ===\n")
 
    A, n = ingresar_matriz()
    imprimir_matriz(A, "A (adyacencia)")
 
    S = calcular_S(A, n)
    

    imprimir_matriz(S, "S (sumatoria final)")
 
    print()
    if es_conexo(S, n):
        print("El grafo es conexo")
    else:
        print("El grafo no es conexo")
main()