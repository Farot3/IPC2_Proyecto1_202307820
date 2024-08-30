from ListaDato import ListaDatos
class NodoGrupo:
    def __init__(self, patron, indices=None, siguiente=None):
        # Inicializa un nodo para agrupar patrones similares
        self.patron = patron  # El patrón que este grupo representa
        self.indices = indices if indices is not None else ListaDatos()  # Índices donde ocurre este patrón
        self.siguiente = siguiente  # Puntero al siguiente grupo