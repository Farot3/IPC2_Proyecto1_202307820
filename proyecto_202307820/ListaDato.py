from NodoDato import Dato

class ListaDatos:
    def __init__(self):
        # Inicializa una lista para almacenar puntos de datos
        self.cabeza = None  # Cabeza de la lista

    def agregar_dato(self, x, y, valor):
        # Agrega un nuevo punto de datos a la lista
        nuevo_nodo = Dato(x, y, valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def obtener_valor(self, x, y):
        # Obtiene el valor en la posición (x, y)
        actual = self.cabeza
        while actual:
            if actual.x == x and actual.y == y:
                return actual.valor
            actual = actual.siguiente
        return 0

    def longitud(self):
        # Obtiene la longitud de la lista
        actual = self.cabeza
        longitud = 0
        while actual:
            longitud += 1
            actual = actual.siguiente
        return longitud