from NodoDato import Dato

class ListaDatos:
    def __init__(self):
        self.cabeza = None

    def agregar_dato(self, x, y, valor):
        nuevo_nodo = Dato(x, y, valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def obtener_valor(self, x, y):
        actual = self.cabeza
        while actual:
            if actual.x == x and actual.y == y:
                return actual.valor
            actual = actual.siguiente
        return 0

    def longitud(self):
        actual = self.cabeza
        longitud = 0
        while actual:
            longitud += 1
            actual = actual.siguiente
        return longitud