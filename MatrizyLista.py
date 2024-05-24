class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def crear_lista_adyacencia(nodos, aristas, dirigido=False):
    lista_adyacencia = [[] for _ in range(len(nodos))]
    for nodo1, nodo2 in aristas:
        lista_adyacencia[nodos.index(nodo1)].append(Nodo(nodo2))
        if not dirigido:
            lista_adyacencia[nodos.index(nodo2)].append(Nodo(nodo1))
    return lista_adyacencia

def imprimir_lista_adyacencia(lista_adyacencia, nodos):
    for i, vecinos in enumerate(lista_adyacencia):
        vecinos_valores = [nodo.valor for nodo in vecinos]
        print(f"{nodos[i]}: {' -> '.join(vecinos_valores)}")

def crear_matriz_adyacencia(nodos, aristas, dirigido=False):
    n = len(nodos)
    matriz_adyacencia = [[0] * n for _ in range(n)]
    for nodo1, nodo2 in aristas:
        i, j = nodos.index(nodo1), nodos.index(nodo2)
        matriz_adyacencia[i][j] = 1
        if not dirigido:
            matriz_adyacencia[j][i] = 1
    return matriz_adyacencia

def imprimir_matriz_adyacencia(nodos, matriz_adyacencia):
    print("  ", " ".join(nodos))
    for i, nodo in enumerate(nodos):
        print(nodo, " ".join(map(str, matriz_adyacencia[i])))

def leer_grafo(separador, dirigido=False):
    nodos = input("Ingresa los nodos del grafo separados por comas (ejemplo: A,B,C,D): ").split(",")
    nodos = [nodo.strip() for nodo in nodos] #Limpia los espacios en blanco y recorre los nodos
    aristas = []
    while True:
        arista = input(f"Ingresa una arista en formato nodo1{separador}nodo2 (ejemplo: A{separador}B), o presiona Enter para finalizar: ").strip()
        if arista == "":
            break
        nodo1, nodo2 = arista.split(separador)
        aristas.append((nodo1.strip(), nodo2.strip()))
    return nodos, aristas, dirigido

def main_lista_adyacencia_dirigido():
    nodos, aristas, dirigido = leer_grafo("->", True) #Dirigido = true: El el grafo es dirigido
    lista_adyacencia = crear_lista_adyacencia(nodos, aristas, dirigido)
    imprimir_lista_adyacencia(lista_adyacencia, nodos)

def main_lista_adyacencia_no_dirigido():
    nodos, aristas, dirigido = leer_grafo("-", False) #Dirigido = false: El grafo no es dirigido
    lista_adyacencia = crear_lista_adyacencia(nodos, aristas, dirigido)
    imprimir_lista_adyacencia(lista_adyacencia, nodos)

def main_matriz_adyacencia_dirigido():
    nodos, aristas, dirigido = leer_grafo("->", True)
    matriz_adyacencia = crear_matriz_adyacencia(nodos, aristas, dirigido)
    imprimir_matriz_adyacencia(nodos, matriz_adyacencia)

def main_matriz_adyacencia_no_dirigido():
    nodos, aristas, dirigido = leer_grafo("-", False)
    matriz_adyacencia = crear_matriz_adyacencia(nodos, aristas, dirigido)
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
            main_lista_adyacencia_dirigido()
        elif opcion == '2':
            main_lista_adyacencia_no_dirigido()
        elif opcion == '3':
            main_matriz_adyacencia_no_dirigido()
        elif opcion == '4':
            main_matriz_adyacencia_dirigido()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

mostrar_menu()
