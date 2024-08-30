from NodoGrupo import NodoGrupo

class ListaGrupos:
    def __init__(self):
        # Inicializa una lista para almacenar grupos
        self.cabeza = None  # Cabeza de la lista

    def agregar_grupo(self, patron, indices):
        # Agrega un nuevo grupo a la lista
        nuevo_nodo = NodoGrupo(patron, indices)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def cantidad_grupos(self):
        # Cuenta el número de grupos
        count = 0
        actual = self.cabeza
        while actual:
            count += 1
            actual = actual.siguiente
        return count

    def obtener_grupo_por_indice(self, indice):
        # Obtiene un grupo por su índice
        actual = self.cabeza
        count = 0
        while actual:
            if count == indice:
                return actual.patron, actual.indices
            count += 1
            actual = actual.siguiente
        return None, None