from ListaFila import ListaFilas
class Matriz:
    def __init__(self, nombre, n, m):
        # Inicializa una matriz
        self.nombre = nombre  # Nombre de la matriz
        self.n = n  # Número de filas
        self.m = m  # Número de columnas
        self.filas = ListaFilas()  # Lista para almacenar filas
        for _ in range(n):
            self.filas.agregar_fila()  # Agrega n filas vacías
        self.matriz_reducida = None  # Almacenará la forma reducida de esta matriz
        self.frecuencias = None  # Almacenará información de frecuencia
        self.siguiente = None  # Puntero a la siguiente matriz en una lista

    def agregar_dato(self, x, y, valor):
        # Agrega un valor a la matriz en la posición (x, y)
        fila_actual = self.filas.cabeza
        for _ in range(x):
            fila_actual = fila_actual.siguiente
        fila_actual.fila.agregar_dato(x, y, valor)

    def obtener_valor(self, x, y):
        # Obtiene el valor en la posición (x, y)
        fila_actual = self.filas.cabeza
        for _ in range(x):
            fila_actual = fila_actual.siguiente
        return fila_actual.fila.datos.obtener_valor(x, y)

    def imprimir(self):
        # Imprime la matriz
        fila_actual = self.filas.cabeza
        for i in range(self.n):
            for j in range(self.m):
                valor = fila_actual.fila.datos.obtener_valor(i, j)
                print(f"{valor:4}", end=" ")
            print()
            fila_actual = fila_actual.siguiente