from NodoMatriz import Matriz
class ListaMatrices:
    def __init__(self):
        self.cabeza = None

    def agregar_matriz(self, nombre, n, m):
        nueva_matriz = Matriz(nombre, n, m)
        if not self.cabeza:
            self.cabeza = nueva_matriz
            nueva_matriz.siguiente = nueva_matriz
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = nueva_matriz
            nueva_matriz.siguiente = self.cabeza
        return nueva_matriz

    def buscar_matriz(self, nombre):
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