import Menu
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
            Menu.opcion_1()
        elif opcion == "2":
            Menu.opcion_2()
        elif opcion == "3":
            Menu.opcion_3()
        elif opcion == "4":
            Menu.opcion_4()
        elif opcion == "5":
            Menu.opcion_salir()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()