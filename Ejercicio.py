class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Función para crear la lista de adyacencia para un grafo dirigido
def crear_lista_adyacencia_dirigido(nodos, aristas):
    lista_adyacencia = [[] for _ in range(len(nodos))]
    for arista in aristas:
        nodo1, nodo2 = arista
        nuevo_nodo = Nodo(nodo2)
        lista_adyacencia[nodos.index(nodo1)].append(nuevo_nodo)
    return lista_adyacencia

# Función para crear la lista de adyacencia para un grafo no dirigido
def crear_lista_adyacencia_no_dirigido(nodos, aristas):
    lista_adyacencia = [[] for _ in range(len(nodos))]
    for arista in aristas:
        nodo1, nodo2 = arista
        nuevo_nodo = Nodo(nodo2)
        lista_adyacencia[nodos.index(nodo1)].append(nuevo_nodo)
        nuevo_nodo = Nodo(nodo1)
        lista_adyacencia[nodos.index(nodo2)].append(nuevo_nodo)
    return lista_adyacencia

# Función para imprimir la lista de adyacencia
def imprimir_lista_adyacencia(lista_adyacencia, nodos):
    for i, vecinos in enumerate(lista_adyacencia): #Vecinos = nodos adyacentes
        vecinos_valores = [nodo.valor for nodo in vecinos] #Se obtienen los valores de los nodos vecinos
        print(f"{nodos[i]}: {' -> '.join(vecinos_valores)}")

# Función para crear la matriz de adyacencia
def crear_matriz_adyacencia(nodos, aristas, dirigido=False):
    n = len(nodos)  # Número de nodos
    matriz_adyacencia = [[0] * n for _ in range(n)]
    
    for arista in aristas:
        nodo1, nodo2 = arista
        i = nodos.index(nodo1) #Para cada arista se obtiene el indice "i" de nodo1
        j = nodos.index(nodo2) #se obtiene el indice "j" del nodo2
        matriz_adyacencia[i][j] = 1
        if not dirigido: #Si no es dirigido se estable la conexión bidireccional entre nodo1 y nodo2
            matriz_adyacencia[j][i] = 1
    return matriz_adyacencia


# Función para imprimir la matriz de adyacencia
def imprimir_matriz_adyacencia(nodos, matriz_adyacencia):
    print("  ", " ".join(nodos))
    for i, nodo in enumerate(nodos): #Enumerate asigna un indice a cada nodo
        print(nodo, " ".join(map(str, matriz_adyacencia[i])))
        
def main_dirigido():
    nodos = input("Ingresa los nodos del grafo separados por comas (ejemplo: A,B,C,D): ").split(",")
    nodos = [nodo.strip() for nodo in nodos]
    aristas = []
    while True:
        arista = input("Ingresa una arista en formato nodo1->nodo2 (ejemplo: A->B), o presiona Enter para finalizar: ").strip()
        if arista == "":
            break
        aristas.append(arista.split("->"))
    lista_adyacencia = crear_lista_adyacencia_dirigido(nodos, aristas)
    imprimir_lista_adyacencia(lista_adyacencia, nodos)

def main_no_dirigido():
    nodos = input("Ingresa los nodos del grafo separados por comas (ejemplo: A,B,C,D): ").split(",") #Split: Divide la cadena
    nodos = [nodo.strip() for nodo in nodos] #Elimina cualquier espacio en blanco
    aristas = []
    while True:
        arista = input("Ingresa una arista en formato nodo1-nodo2 (ejemplo: A-B), o presiona Enter para finalizar: ").strip()
        if arista == "":
            break
        aristas.append(arista.split("-"))
    lista_adyacencia = crear_lista_adyacencia_no_dirigido(nodos, aristas)
    imprimir_lista_adyacencia(lista_adyacencia, nodos)

def mainMatrizAdyacencia():
    nodos = input("Ingresa los nodos del grafo separados por comas (ejemplo: A,B,C,D): ").split(",")
    nodos = [nodo.strip() for nodo in nodos]
    aristas = []
    while True:
        arista = input("Ingresa una arista en formato nodo1-nodo2 (ejemplo: A-B), o presiona Enter para finalizar: ").strip()
        if arista == "":
            break
        nodo1, nodo2 = arista.split("-")
        aristas.append((nodo1.strip(), nodo2.strip()))
    matriz_adyacencia = crear_matriz_adyacencia(nodos, aristas)
    imprimir_matriz_adyacencia(nodos, matriz_adyacencia)

def mainDirigidoMatriz():
    nodos = input("Ingresa los nodos del grafo separados por comas (ejemplo: A,B,C,D): ").split(",")
    nodos = [nodo.strip() for nodo in nodos] #Strip: Elimina espacios en blanco
    aristas = []
    while True:
        arista = input("Ingresa una arista en formato nodo1->nodo2 (ejemplo: A->B), o presiona Enter para finalizar: ").strip()
        if arista == "":
            break
        nodo1, nodo2 = arista.split("->")
        aristas.append((nodo1.strip(), nodo2.strip()))
    matriz_adyacencia = crear_matriz_adyacencia(nodos, aristas, dirigido=True)
    imprimir_matriz_adyacencia(nodos, matriz_adyacencia)

def mostrar_menu():
    while True:
        print("\n--- Menú ---")
        print("1. Crear lista de adyacencia para grafo dirigido")
        print("2. Crear lista de adyacencia para grafo no dirigido")
        print("3. Crear matriz de adyacencia para grafo no dirigido")
        print("4. Crear matriz de adyacencia para grafo dirigido")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            main_dirigido()
        elif opcion == '2':
            main_no_dirigido()
        elif opcion == '3':
            mainMatrizAdyacencia()
        elif opcion == '4':
            mainDirigidoMatriz()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Mostrar el menú
mostrar_menu()