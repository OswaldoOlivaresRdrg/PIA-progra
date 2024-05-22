
def ImpresionArchivo():
    while True:
        Archivo = open("PIA.txt", "r") 
        print(Archivo.read())
        Archivo.close()
        input("Pulse Enter para continuar...")
        break
