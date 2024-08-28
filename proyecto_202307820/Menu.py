import xml.etree.ElementTree as ET
from ProcesoArchivo import ProcesadorArchivo
def imprimirXML(ruta):
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        return ET.tostring(root, encoding='unicode')
    except Exception as e:
        print(f"Error al leer el archivo XML: {e}")
        return None

def menu():
    paco = ""
    procesador = ProcesadorArchivo()

    while True:
        print("\nMenu principal:")
        print("-----------------------------------------------")
        print("     1. Cargar archivo")
        print("     2. Procesar archivo")
        print("     3. Escribir archivo salida")
        print("     4. Mostrar datos del estudiante")
        print("     5. Generar gráfica")
        print("     6. Salir")
        print("------------------------------------------------")
        macaco = int(input("Escribe una opción:  "))

        if macaco == 1:
            print("------------------------------------------------")
            paco = input("Ingrese la ruta del archivo: ")
            print(f"Ruta ingresada {paco}")
            print("------------------------------------------------")
        elif macaco == 2:
            print("------------------------------------------------")
            if paco:
                contenido_xml = imprimirXML(paco)
                if contenido_xml:
                    procesador.procesar_archivo(contenido_xml)
                    procesador.procesar_matrices()
            else:
                print("Primero debe cargar un archivo.")
            print("------------------------------------------------")
        elif macaco == 3:
            if procesador.lista_matrices.cabeza:
                directorio = input("Ingrese la ruta del directorio donde desea guardar los archivos: ")
                procesador.exportar_todas_matrices(directorio)
            else:
                print("No hay matrices procesadas para exportar.")
        elif macaco == 4:
            print("\nOttoniel Fabricio Vásquez Pineda")
            print("202307820")
            print("Introducción a la Programación y computación 2 sección B")
            print("Ingenieria en Ciencias y Sistemas")
            print("4to semestre")
            print("https://github.com/Farot3/IPC2_Proyecto1_202307820")
        elif macaco == 5:
            pass  # Implementar la generación de gráficas
        elif macaco == 6:
            print("Se salió del Menu")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()