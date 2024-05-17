import menu
import os
def main():
    while True:
        os.system("cls")
        print("=== MENÚ ===")
        print("1. Consulta Web")
        print("2. Consulta local")
        print("3. Graficas")
        print("4. Borrar info")
        print("5. Salir")
        Opcion = input("Seleccione una opción: ")

        if Opcion == "1":
            menu.Opcion_1()
        elif Opcion == "2":
            menu.Opcion_2()
        elif Opcion == "3":
            menu.Opcion_3()
        elif Opcion == "4":
            menu.Opcion_4()
        elif Opcion == "5":
            menu.Opcion_salir()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()