from NodoGrupo import NodoGrupo
class ListaGrupos:
    def __init__(self):
        self.cabeza = None

    def agregar_grupo(self, patron, indices):
        nuevo_nodo = NodoGrupo(patron, indices)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def cantidad_grupos(self):
        count = 0
        actual = self.cabeza
        while actual:
            count += 1
            actual = actual.siguiente
        return count

    def obtener_grupo_por_indice(self, indice):
        actual = self.cabeza
        count = 0
        while actual:
            if count == indice:
                return actual.patron, actual.indices
            count += 1
            actual = actual.siguiente
        return None, None