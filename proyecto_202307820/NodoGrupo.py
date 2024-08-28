from ListaDato import ListaDatos
class NodoGrupo:
    def __init__(self, patron, indices=None, siguiente=None):
        self.patron = patron
        self.indices = indices if indices is not None else ListaDatos()
        self.siguiente = siguiente