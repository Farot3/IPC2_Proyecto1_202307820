from NodoFila import NodoFila
from ListaDato import ListaDatos

class ListaFilas:
    def __init__(self):
        # Inicializa una lista para almacenar filas
        self.cabeza = None  # Cabeza de la lista
        self.cola = None  # Cola de la lista

    def agregar_fila(self):
        # Agrega una nueva fila a la lista
        nueva_fila = Fila()
        nuevo_nodo = NodoFila(nueva_fila)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        return nueva_fila

class Fila:
    def __init__(self):
        # Inicializa una fila
        self.datos = ListaDatos()  # Lista para almacenar datos en esta fila

    def agregar_dato(self, x, y, valor):
        # Agrega un nuevo punto de datos a la fila
        self.datos.agregar_dato(x, y, valor)