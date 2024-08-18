def menu():
    while True:
        print("Menu principal:")
        print("     1. Cargar archivo")
        print("     2. Procesar archivo")
        print("     3. Escribir archivo salida")
        print("     4. Mostrar datos del estudiante")
        print("     5. Generar gráfica")
        print("     6. Salir")
        macaco = int(input("Escribe una opción:  "))

        if macaco == 1:
            paco = input("Ingrese la ruta del archivo: ")
        elif macaco == 2:
            pass
        elif macaco == 3:
            pass
        elif macaco == 4:
            print(" ")
            print("Ottoniel Fabricio Vásquez Pineda")
            print("202307820")
            print("Introducción a la Programación y computación 2 sección B")
            print("Ingenieria en Ciencias y Sistemas")
            print("4to semestre")
            print(" ")
        elif macaco == 5:
            pass
        elif macaco == 6:
            print("Se salio del Menu")
            break
        else:
            print("opción invalida")




if __name__ == "__main__":
    menu()