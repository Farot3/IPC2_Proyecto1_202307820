class NodoMatrizReducida:
    def __init__(self, x, y, valor):
        # Inicializa un nodo para la matriz reducida
        self.x = x  # Índice de fila
        self.y = y  # Índice de columna
        self.valor = valor  # Valor en esta posición
        self.siguiente = None  # Puntero al siguiente nodo en la misma fila
        self.abajo = None  # Puntero al nodo debajo en la misma columna