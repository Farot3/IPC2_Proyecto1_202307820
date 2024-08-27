from NodoMatriz import Matriz

class ListaMatrices:
    def __init__(self):
        self.cabeza = None

    def agregar_matriz(self, nombre, n, m):
        nuevo_nodo = Matriz(nombre, n, m)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo  # Hacemos la lista circular
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

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