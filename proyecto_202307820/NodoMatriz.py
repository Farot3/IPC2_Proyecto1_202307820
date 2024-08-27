class Matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.matriz = [[0 for _ in range(m)] for _ in range(n)]
        self.matriz_reducida = None
        self.next = None