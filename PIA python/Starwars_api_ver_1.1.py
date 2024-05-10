import menu
import os
def main():
    while True:
        os.system("cls")
        print("=== MENÚ ===")
        print("1. Personajes")
        print("2. Naves")
        print("3. Animales")
        print("4. Archivos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu.opcion_1()
        elif opcion == "2":
            menu.opcion_2()
        elif opcion == "3":
            menu.opcion_3()
        elif opcion == "4":
            menu.opcion_4()
        elif opcion == "5":
            menu.opcion_salir()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()