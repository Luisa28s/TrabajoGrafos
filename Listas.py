class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.liga = None

class Lista:
    def __init__(self, vertices):
        self.V = vertices
        self.lista_ady = [None] * self.V

    def agregar(self, inicio, llegada):
        nodo = Nodo(llegada)
        nodo.liga = self.lista_ady[inicio]
        self.lista_ady[inicio] = nodo

        nodo = Nodo(inicio)
        nodo.liga = self.lista_ady[llegada]
        self.lista_ady[llegada] = nodo

    def agregarDirigido(self, inicio, llegada):
        nodo = Nodo(llegada)
        nodo.liga = self.lista_ady[inicio]
        self.lista_ady[inicio] = nodo

    def imprimir_grafo(self):
        for v in range(self.V):
            print(f"Lista de adyacencia del vértice {v+1}: ", end="")
            temp = self.lista_ady[v]
            adyacentes = []
            while temp:
                adyacentes.append(temp.dato)
                temp = temp.liga
            adyacentes.sort()
            for dato in adyacentes:
                print(f"->{dato + 1}", end="")
            print("")



while True:
    print("Escoja que grafo quiere ver")
    print("1. G1")
    print("2. G2")
    print("3. G3")
    opc=int(input("Ingrese su opcion "))
    
    if opc == 1:
        V = 4
        aristas = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        grafo = Lista(V)
        for arista in aristas:
            grafo.agregar(arista[0]-1, arista[1]-1)
    elif opc == 2:
        V = 7
        aristas = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
        grafo = Lista(V)
        for arista in aristas:
            grafo.agregar(arista[0]-1, arista[1]-1)
    elif opc == 3:
        V = 3
        aristas = [(1, 2), (2, 1), (2, 3), (3, 1)]
        grafo = Lista(V)
        for arista in aristas:
            grafo.agregarDirigido(arista[0]-1, arista[1]-1)
    else:
        print("Opción no válida.")
        break

    

    grafo.imprimir_grafo()