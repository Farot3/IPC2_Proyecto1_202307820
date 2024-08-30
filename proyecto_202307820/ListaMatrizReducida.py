from NodoMatrizReducida import NodoMatrizReducida

class ListaMatrizReducida:
    def __init__(self):
        # Inicializa una matriz reducida
        self.cabeza = None  # Cabeza de la matriz
        self.filas = 0  # Número de filas
        self.columnas = 0  # Número de columnas

    def agregar_dato(self, x, y, valor):
        # Agrega un nuevo punto de datos a la matriz reducida
        nuevo_nodo = NodoMatrizReducida(x, y, valor)

        # Actualiza el conteo de filas y columnas
        self.filas = max(self.filas, x + 1)
        self.columnas = max(self.columnas, y + 1)

        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return

        if x > self._ultima_fila().x:
            self._ultima_fila().abajo = nuevo_nodo
        else:
            fila_actual = self.cabeza
            while fila_actual.abajo and fila_actual.abajo.x <= x:
                fila_actual = fila_actual.abajo

            if fila_actual.x == x:
                while fila_actual.siguiente and fila_actual.siguiente.y < y:
                    fila_actual = fila_actual.siguiente
                nuevo_nodo.siguiente = fila_actual.siguiente
                fila_actual.siguiente = nuevo_nodo
            else:
                nuevo_nodo.abajo = fila_actual.abajo
                fila_actual.abajo = nuevo_nodo

    def obtener_valor(self, x, y):
        # Obtiene el valor en la posición (x, y)
        fila_actual = self.cabeza
        while fila_actual and fila_actual.x < x:
            fila_actual = fila_actual.abajo

        if fila_actual and fila_actual.x == x:
            nodo_actual = fila_actual
            while nodo_actual and nodo_actual.y < y:
                nodo_actual = nodo_actual.siguiente

            if nodo_actual and nodo_actual.y == y:
                return nodo_actual.valor

        return 0

    def _ultima_fila(self):
        # Obtiene la última fila de la matriz
        if not self.cabeza:
            return None
        fila_actual = self.cabeza
        while fila_actual.abajo:
            fila_actual = fila_actual.abajo
        return fila_actual

    def imprimir(self):
        # Imprime la matriz reducida
        for i in range(self.filas):
            for j in range(self.columnas):
                print(f"{self.obtener_valor(i, j):4}", end=" ")
            print()