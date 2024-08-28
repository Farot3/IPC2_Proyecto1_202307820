from ListaMatriz import ListaMatrices
import os
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET
from ListaFila import ListaFilas
from ListaDato import ListaDatos
from ListaMatrizReducida import ListaMatrizReducida
from ListasGrupo import ListaGrupos
class ProcesadorArchivo:
    def __init__(self):
        self.lista_matrices = ListaMatrices()

    def procesar_archivo(self, contenido_xml):
        try:
            root = ET.fromstring(contenido_xml)

            for matriz_elem in root.findall('matriz'):
                nombre = matriz_elem.get('nombre')
                n = int(matriz_elem.get('n'))
                m = int(matriz_elem.get('m'))

                if self.lista_matrices.buscar_matriz(nombre):
                    print(f"Advertencia: Ya existe una matriz con el nombre '{nombre}'. Se omitirá.")
                    continue

                nueva_matriz = self.lista_matrices.agregar_matriz(nombre, n, m)

                for dato_elem in matriz_elem.findall('dato'):
                    x = int(dato_elem.get('x')) - 1
                    y = int(dato_elem.get('y')) - 1
                    valor = int(dato_elem.text)

                    if 0 <= x < n and 0 <= y < m:
                        nueva_matriz.agregar_dato(x, y, valor)
                    else:
                        print(
                            f"Error con la matriz: '{nombre}': Los datos son mayores que los atributos n o m x={x + 1}, y={y + 1}")
                print(f"\nEl archivo {nombre} ha sido procesado\n")
            print("------------------------------------------------")
            print("Los o el archivo(S) ha sido procesado.")

        except ET.ParseError:
            print("Error: El archivo XML no es válido.")
        except ValueError:
            print("Error: Valores no válidos en el archivo XML.")
        except Exception as e:
            print(f"Error inesperado al procesar el archivo: {str(e)}")

    def procesar_matrices(self):
        if not self.lista_matrices.cabeza:
            print("No hay matrices para procesar.")
            return

        matriz_actual = self.lista_matrices.cabeza
        while True:
            print("------------------------------------------------")
            print(f"Calculando la matriz binaria: {matriz_actual.nombre} ....\n")
            patron_acceso = self.convertir_a_patron_acceso(matriz_actual)
            grupos = self.agrupar_tuplas(patron_acceso)
            print("Realizando suma de tuplas....")
            print("------------------------------------------------")
            matriz_reducida, frecuencias = self.crear_matriz_reducida(matriz_actual, grupos)

            matriz_actual.matriz_reducida = matriz_reducida
            matriz_actual.frecuencias = frecuencias

            self.imprimir_matrices(matriz_actual, matriz_reducida, frecuencias)

            matriz_actual = matriz_actual.siguiente
            if matriz_actual == self.lista_matrices.cabeza:
                break
        print("\n------------------------------------------------")
        print("Todas las matrices han sido procesadas.")

    def convertir_a_patron_acceso(self, matriz):
        patron = ListaFilas()
        for i in range(matriz.n):
            fila = patron.agregar_fila()
            for j in range(matriz.m):
                fila.agregar_dato(i, j, 1 if matriz.obtener_valor(i, j) > 0 else 0)
        return patron

    def agrupar_tuplas(self, patron_acceso):
        lista_grupos = ListaGrupos()
        fila_actual = patron_acceso.cabeza
        i = 0
        while fila_actual:
            patron = ListaDatos()
            dato_actual = fila_actual.fila.datos.cabeza
            while dato_actual:
                patron.agregar_dato(dato_actual.x, dato_actual.y, dato_actual.valor)
                dato_actual = dato_actual.siguiente
            patron_tuple = self.lista_a_tupla(patron)

            grupo_encontrado = False
            grupo_actual = lista_grupos.cabeza
            while grupo_actual:
                if grupo_actual.patron == patron_tuple:
                    grupo_actual.indices.agregar_dato(0, 0, i)
                    grupo_encontrado = True
                    break
                grupo_actual = grupo_actual.siguiente

            if not grupo_encontrado:
                nueva_lista = ListaDatos()
                nueva_lista.agregar_dato(0, 0, i)
                lista_grupos.agregar_grupo(patron_tuple, nueva_lista)

            fila_actual = fila_actual.siguiente
            i += 1

        return lista_grupos

    def lista_a_tupla(self, lista):
        resultado = ()
        dato_actual = lista.cabeza
        while dato_actual:
            resultado += (dato_actual.valor,)
            dato_actual = dato_actual.siguiente
        return resultado

    def crear_matriz_reducida(self, matriz_original, lista_grupos):
        matriz_reducida = ListaMatrizReducida()
        frecuencias = ListaDatos()

        num_filas_reducidas = lista_grupos.cantidad_grupos()
        num_columnas_reducidas = matriz_original.m

        for i in range(num_filas_reducidas):
            patron, indices = lista_grupos.obtener_grupo_por_indice(i)
            for j in range(num_columnas_reducidas):
                suma = 0
                indice_actual = indices.cabeza
                while indice_actual:
                    valor = matriz_original.obtener_valor(indice_actual.valor, j)
                    suma += valor
                    indice_actual = indice_actual.siguiente
                matriz_reducida.agregar_dato(i, j, suma)

            frecuencias.agregar_dato(0, frecuencias.longitud(), indices.longitud())

        print("Matriz reducida creada con éxito.")
        print("------------------------------------------------")
        return matriz_reducida, frecuencias

    def imprimir_matrices(self, matriz_original, matriz_reducida, frecuencias):
        print(f"Matriz: {matriz_original.nombre}")
        print(f"Dimensiones originales: {matriz_original.n} x {matriz_original.m}")
        print("Matriz original:")
        print("------------------------------------------------")
        matriz_original.imprimir()
        print("------------------------------------------------")

        print("Matriz reducida:")
        print("------------------------------------------------")
        matriz_reducida.imprimir()
        print("------------------------------------------------")

        print("Frecuencias de grupos:")
        freq_actual = frecuencias.cabeza
        while freq_actual:
            print(f"{freq_actual.valor}", end=" ")
            freq_actual = freq_actual.siguiente

    def escribir_archivo_salida(self, matriz_original, matriz_reducida, frecuencias, ruta_completa):
        doc = minidom.Document()

        root = doc.createElement("matriz")
        doc.appendChild(root)

        root.setAttribute("nombre", f"{matriz_original.nombre}_Salida")
        root.setAttribute("n", str(matriz_reducida.filas))
        root.setAttribute("m", str(matriz_reducida.columnas))
        root.setAttribute("g", str(frecuencias.longitud()))

        for i in range(matriz_reducida.filas):
            for j in range(matriz_reducida.columnas):
                dato_elem = doc.createElement("dato")
                dato_elem.setAttribute("x", str(i + 1))
                dato_elem.setAttribute("y", str(j + 1))
                dato_text = doc.createTextNode(str(matriz_reducida.obtener_valor(i, j)))
                dato_elem.appendChild(dato_text)
                root.appendChild(dato_elem)

        freq_actual = frecuencias.cabeza
        g = 1
        while freq_actual:
            freq_elem = doc.createElement("frecuencia")
            freq_elem.setAttribute("g", str(g))
            freq_text = doc.createTextNode(str(freq_actual.valor))
            freq_elem.appendChild(freq_text)
            root.appendChild(freq_elem)
            freq_actual = freq_actual.siguiente
            g += 1

        xml_str = doc.toprettyxml(indent="    ")
        with open(ruta_completa, "w", encoding="utf-8") as f:
            f.write(xml_str)

        print(f"Archivo XML '{ruta_completa}' escrito exitosamente.")

    def exportar_todas_matrices(self, directorio):
        if not self.lista_matrices.cabeza:
            print("No hay matrices para exportar.")
            return

        if not os.path.exists(directorio):
            os.makedirs(directorio)

        matriz_actual = self.lista_matrices.cabeza
        while True:
            if matriz_actual.matriz_reducida and matriz_actual.frecuencias:
                nombre_archivo = input(
                    f"Ingrese el nombre del archivo para la matriz '{matriz_actual.nombre}' (sin extensión): ")
                nombre_archivo = f"{nombre_archivo}.xml"
                ruta_completa = os.path.join(directorio, nombre_archivo)
                self.escribir_archivo_salida(
                    matriz_original=matriz_actual,
                    matriz_reducida=matriz_actual.matriz_reducida,
                    frecuencias=matriz_actual.frecuencias,
                    ruta_completa=ruta_completa
                )
            else:
                print(f"La matriz '{matriz_actual.nombre}' no ha sido procesada y no se puede exportar.")

            matriz_actual = matriz_actual.siguiente
            if matriz_actual == self.lista_matrices.cabeza:
                break

        print("Todas las matrices procesadas han sido exportadas.")