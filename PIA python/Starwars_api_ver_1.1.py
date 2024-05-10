import opciones
import menu
import Archivos

def main():
    while True:
        opcion = menu.mostrar_menu()

        if opcion == "1":
            opciones.opcion1()
        elif opcion == "2":
            opciones.opcion2()
        elif opcion == "3":
            opciones.opcion3()
        elif opcion == "4":
            opciones.opcion4()
        elif opcion == "5":
            opciones.opcion_salir()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()