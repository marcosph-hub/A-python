import heapq
def leer_grafo(fichero):
    with open(fichero, 'r') as f:
        n = int(f.readline().strip())
        distancias = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            distancias[i][i] = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                d = int(f.readline().strip())
                if d != -1:
                    distancias[i][j] = d
                    distancias[j][i] = d
                    
    return distancias

def leer_heuristica(fichero):
    with open(fichero, 'r') as f:
        n = int(f.readline().strip())
        heuristica = []
        for _ in range(n):
            h = int(f.readline().strip())
            heuristica.append(h)
            
    return heuristica


import heapq

def a_star(grafo, heuristica, inicio, fin):
    n = len(grafo)
    abiertos = [(heuristica[inicio], 0, inicio, [])]  # (f_function, g_score, nodo, camino)
    cerrados = set()
    costos = {inicio: 0}
    iterations = 0
    
    while abiertos:
        iterations += 1
        _, costo_actual, nodo_actual, camino = heapq.heappop(abiertos)
        
        if nodo_actual in cerrados:
            continue
        
        camino = camino + [nodo_actual]
        
        if nodo_actual == fin:
            return camino, costo_actual, iterations
        
        cerrados.add(nodo_actual)
        
        for vecino in range(n):
            if grafo[nodo_actual][vecino] != float('inf'):
                nuevo_costo = costo_actual + grafo[nodo_actual][vecino]
                
                if vecino in costos and nuevo_costo >= costos[vecino]:
                    continue
                
                costos[vecino] = nuevo_costo
                f_function = nuevo_costo + heuristica[vecino]
                heapq.heappush(abiertos, (f_function, nuevo_costo, vecino, camino))
    
    return None, float('inf')

#def write(camino_min, costo, iterations):


def main():
    grafo = leer_grafo('instance_A_star.txt')
    heuristica = leer_heuristica('h_instance_A_star.txt')

    inicio = int(input("Introduce el nodo de inicio: "))
    fin = int(input("Introduce el nodo de destino: "))
    
    camino, costo, iterations = a_star(grafo, heuristica, inicio - 1, fin - 1)
    camino = [valor + 1 for valor in camino]
    print("\nNodo Inicial: ", inicio)
    print("Nodo Final: ", fin)
    print("Camino:", camino)
    print("Costo:", costo)
    print("Iteraciones:", iterations)

if __name__ == '__main__':
    main()
