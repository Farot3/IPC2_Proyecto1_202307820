from NodoFila import NodoFila
from ListaDato import ListaDatos
class ListaFilas:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_fila(self):
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
        self.datos = ListaDatos()

    def agregar_dato(self, x, y, valor):
        self.datos.agregar_dato(x, y, valor)