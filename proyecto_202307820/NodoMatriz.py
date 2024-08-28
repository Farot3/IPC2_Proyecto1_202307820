from ListaFila import ListaFilas

class Matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n  # n ahora representa filas
        self.m = m  # m ahora representa columnas
        self.filas = ListaFilas()
        for _ in range(n):
            self.filas.agregar_fila()
        self.matriz_reducida = None
        self.frecuencias = None
        self.siguiente = None

    def agregar_dato(self, x, y, valor):
        fila_actual = self.filas.cabeza
        for _ in range(x):
            fila_actual = fila_actual.siguiente
        fila_actual.fila.agregar_dato(x, y, valor)

    def obtener_valor(self, x, y):
        fila_actual = self.filas.cabeza
        for _ in range(x):
            fila_actual = fila_actual.siguiente
        return fila_actual.fila.datos.obtener_valor(x, y)

    def imprimir(self):
        fila_actual = self.filas.cabeza
        for i in range(self.n):  # n ahora representa filas
            for j in range(self.m):  # m ahora representa columnas
                valor = fila_actual.fila.datos.obtener_valor(i, j)
                print(f"{valor:4}", end=" ")
            print()
            fila_actual = fila_actual.siguiente