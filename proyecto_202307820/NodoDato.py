class Dato:
    def __init__(self, x, y, valor):
        # Inicializa un punto de datos en la matriz
        self.x = x  # Índice de fila
        self.y = y  # Índice de columna
        self.valor = valor  # Valor en esta posición
        self.siguiente = None  # Puntero al siguiente punto de datos