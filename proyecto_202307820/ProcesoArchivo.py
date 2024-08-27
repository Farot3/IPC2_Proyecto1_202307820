from ListaMatriz import ListaMatrices
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET

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

                self.lista_matrices.agregar_matriz(nombre, n, m)
                matriz_actual = self.lista_matrices.buscar_matriz(nombre)

                for dato_elem in matriz_elem.findall('dato'):
                    x = int(dato_elem.get('x')) - 1
                    y = int(dato_elem.get('y')) - 1
                    valor = int(dato_elem.text)

                    if 0 <= x < n and 0 <= y < m:
                        matriz_actual.matriz[x][y] = valor
                    else:
                        print(f"Error con la matriz: '{nombre}': Los datos son mayores que los atributos n o m x={x + 1}, y={y + 1}")
                print("------------------------------------------------")
                print(f">El archivo {nombre} ha sido procesado exitosamente")

            print(">El archivo ha sido procesado.")

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
            print(f"Calculando la matriz binaria: {matriz_actual.nombre} ....")

            patron_acceso = self.convertir_a_patron_acceso(matriz_actual.matriz)
            grupos = self.agrupar_tuplas(patron_acceso)
            print("------------------------------------------------")
            print("Realizando suma de tuplas....")
            matriz_reducida, frecuencias = self.crear_matriz_reducida(matriz_actual.matriz, grupos)

            matriz_actual.matriz_reducida = matriz_reducida
            matriz_actual.frecuencias = frecuencias

            matriz_actual = matriz_actual.siguiente
            if matriz_actual == self.lista_matrices.cabeza:
                break
        print("------------------------------------------------")
        print("Todas las matrices han sido procesadas.")

    def convertir_a_patron_acceso(self, matriz):
        return [[1 if valor > 0 else 0 for valor in fila] for fila in matriz]

    def agrupar_tuplas(self, patron_acceso):
        grupos = {}
        for i, patron in enumerate(patron_acceso):
            patron_tuple = tuple(patron)
            if patron_tuple in grupos:
                grupos[patron_tuple].append(i)
            else:
                grupos[patron_tuple] = [i]
        return grupos

    def crear_matriz_reducida(self, matriz_original, grupos):
        matriz_reducida = []
        frecuencias = []
        for indices in grupos.values():
            fila_reducida = [sum(matriz_original[i][j] for i in indices) for j in range(len(matriz_original[0]))]
            matriz_reducida.append(fila_reducida)
            frecuencias.append(len(indices))
        return matriz_reducida, frecuencias

    def imprimir_matrices(self):
        if not self.lista_matrices.cabeza:
            print("No hay matrices para imprimir.")
            return

        matriz_actual = self.lista_matrices.cabeza
        while True:
            print("------------------------------------------------")
            print(f"Matriz: {matriz_actual.nombre}")
            print(f"Dimensiones originales: {matriz_actual.n} x {matriz_actual.m}")
            print("Matriz original:")
            for fila in matriz_actual.matriz:
                print(" ".join(map(str, fila)))

            if matriz_actual.matriz_reducida:
                print(f"\n------------------------------------------------")
                print("Matriz reducida:")
                for fila in matriz_actual.matriz_reducida:
                    print(" ".join(map(str, fila)))
                print(f"Frecuencias de grupos: {matriz_actual.frecuencias}")
            else:
                print("La matriz reducida aún no ha sido calculada.")

            matriz_actual = matriz_actual.siguiente
            if matriz_actual == self.lista_matrices.cabeza:
                break

    def escribir_archivo_salida(self, nombre_archivo):
        if not self.lista_matrices.cabeza:
            print("No hay matrices para escribir en el archivo de salida.")
            return

        root = ET.Element("matrices")

        matriz_actual = self.lista_matrices.cabeza
        while True:
            if matriz_actual.matriz_reducida:
                matriz_elem = ET.SubElement(root, "matriz")
                matriz_elem.set("nombre", f"{matriz_actual.nombre}")
                matriz_elem.set("n", str(len(matriz_actual.matriz_reducida)))
                matriz_elem.set("m", str(len(matriz_actual.matriz_reducida[0])))
                matriz_elem.set("g", str(len(matriz_actual.frecuencias)))

                for i, fila in enumerate(matriz_actual.matriz_reducida):
                    for j, valor in enumerate(fila):
                        dato_elem = ET.SubElement(matriz_elem, "dato")
                        dato_elem.set("x", str(i + 1))
                        dato_elem.set("y", str(j + 1))
                        dato_elem.text = str(valor)

                for i, freq in enumerate(matriz_actual.frecuencias):
                    freq_elem = ET.SubElement(matriz_elem, "frecuencia")
                    freq_elem.set("g", str(i + 1))
                    freq_elem.text = str(freq)

            matriz_actual = matriz_actual.siguiente
            if matriz_actual == self.lista_matrices.cabeza:
                break

        # Crear un string XML formateado
        xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")

        # Escribir el XML en un archivo
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            f.write(xml_str)

        print(f"Archivo de salida '{nombre_archivo}' creado exitosamente.")