class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def __str__(self):
        return str(self.valor) #Imprime un objeto de la clase nodo como una cadena

# Función para crear la lista de adyacencia para un grafo dirigido
def crear_lista_adyacencia_dirigido(nodos, aristas):
    lista_adyacencia = [[] for _ in range(len(nodos))]
    for nodo1, nodo2 in aristas:
        indice_nodo1 = nodos.index(nodo1)
        lista_adyacencia[indice_nodo1].append(Nodo(nodo2))
    return lista_adyacencia

# Función para crear la lista de adyacencia para un grafo no dirigido
def crear_lista_adyacencia_no_dirigido(nodos, aristas):
    lista_adyacencia = [[] for _ in range(len(nodos))]
    for nodo1, nodo2 in aristas:
        indice_nodo1 = nodos.index(nodo1)
        indice_nodo2 = nodos.index(nodo2)
        lista_adyacencia[indice_nodo1].append(Nodo(nodo2))
        lista_adyacencia[indice_nodo2].append(Nodo(nodo1))
    return lista_adyacencia

# Función para imprimir la lista de adyacencia
def imprimir_lista_adyacencia(lista_adyacencia, nodos):
    for i, vecinos in enumerate(lista_adyacencia):
        vecinos_valores = [nodo.valor for nodo in vecinos]
        print(f"{nodos[i]}: {' -> '.join(vecinos_valores)}")

# Función para crear la matriz de adyacencia
def crear_matriz_adyacencia(nodos, aristas):
    n = len(nodos)  # Número de nodos
    matriz_adyacencia = [[0] * n for _ in range(n)]
    
    for arista in aristas:
        if arista:  # Verificar si la entrada no está vacía
            nodo1, nodo2 = arista
            i = nodos.index(nodo1) 
            j = nodos.index(nodo2) 
            matriz_adyacencia[i][j] = 1
            if arista[::-1] not in aristas:  # Verificar si la arista inversa no está en la lista
                matriz_adyacencia[j][i] = 1  # Si no está, es un grafo no dirigido
    return matriz_adyacencia


# Función para imprimir la matriz de adyacencia
def imprimir_matriz_adyacencia(nodos, matriz_adyacencia):
    print("  ", " ".join(nodos))
    for i, nodo in enumerate(nodos):
        print(nodo, " ".join(map(str, matriz_adyacencia[i])))
        
def menu():
    while True:
        print("********************* Menú *************************")
        print("1. Crear lista de adyacencia para grafo dirigido")
        print("2. Crear lista de adyacencia para grafo no dirigido")
        print("3. Crear matriz de adyacencia para grafo dirigido")
        print("4. Crear matriz de adyacencia para grafo no dirigido")
        print("5. Salir")
        print("*******************************************************")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            nodos = input("Ingrese los nodos del grafo separados por comas: ").split(",")
            nodos = [nodo.strip() for nodo in nodos]
            aristas = []
            while True:
                arista = input("Ingresa una arista en formato nodo1-nodo2 o presione Enter para finalizar: ").strip()
                if arista == "":
                    break
                aristas.append(arista.split("-"))
            lista_adyacencia = crear_lista_adyacencia_dirigido(nodos, aristas)
            imprimir_lista_adyacencia(lista_adyacencia, nodos)
        elif opcion == '2':
            nodos = input("Ingresa los nodos del grafo separados por comas: ").split(",")
            nodos = [nodo.strip() for nodo in nodos]
            aristas = []
            while True:
                arista = input("Ingresa una arista en formato nodo1-nodo2 o presione Enter para finalizar: ").strip()
                if arista == "":
                    break
                aristas.append(arista.split("-"))
            lista_adyacencia = crear_lista_adyacencia_no_dirigido(nodos, aristas)
            imprimir_lista_adyacencia(lista_adyacencia, nodos)
        elif opcion == '3':
            nodos = input("Ingresa los nodos del grafo separados por comas: ").split(",")
            nodos = [nodo.strip() for nodo in nodos]
            aristas = []
            while True:
                arista = input("Ingresa una arista en formato nodo1->nodo2 o presione Enter para finalizar: ").strip()
                if arista == "":
                    break
                aristas.append(arista.split("-"))
            matriz_adyacencia = crear_matriz_adyacencia(nodos, aristas)
            imprimir_matriz_adyacencia(nodos, matriz_adyacencia)
        elif opcion == '4':
            nodos = input("Ingresa los nodos del grafo separados por comas: ").split(",")
            nodos = [nodo.strip() for nodo in nodos]
            aristas = []
            while True:
                arista = input("Ingresa una arista en formato nodo1-nodo2 o presiona Enter para finalizar: ").strip()
                if arista == "":
                    break
                aristas.append(arista.split("-"))
            matriz_adyacencia = crear_matriz_adyacencia(nodos, aristas)
            imprimir_matriz_adyacencia(nodos, matriz_adyacencia)
        elif opcion == '5':
            print("Salida del programa")
            break
        else:
            print("Opción no válida.")

menu()
