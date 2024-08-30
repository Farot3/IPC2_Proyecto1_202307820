from NodoMatriz import Matriz

class ListaMatrices:
    def __init__(self):
        # Inicializa una lista para almacenar matrices
        self.cabeza = None  # Cabeza de la lista

    def agregar_matriz(self, nombre, n, m):
        # Agrega una nueva matriz a la lista
        nueva_matriz = Matriz(nombre, n, m)
        if not self.cabeza:
            self.cabeza = nueva_matriz
            nueva_matriz.siguiente = nueva_matriz  # Lista circular
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = nueva_matriz
            nueva_matriz.siguiente = self.cabeza
        return nueva_matriz

    def buscar_matriz(self, nombre):
        # Busca una matriz por nombre
        if not self.cabeza:
            return None
        temp = self.cabeza
        while True:
            if temp.nombre == nombre:
                return temp
            temp = temp.siguiente
            if temp == self.cabeza:
                break
        return None