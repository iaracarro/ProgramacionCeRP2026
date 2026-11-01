# Desafio 38

import os

nombre_archivo = "mi_texto.txt"

opcion = input("¿Querés guardar (g) o leer (l) un archivo? ").lower()

if opcion == "g":
    texto = input("Escribí tu texto: ")

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(texto)

    print("Archivo guardado correctamente.")
    print("Ubicación:", os.path.abspath(nombre_archivo))

elif opcion == "l":
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            print(archivo.read())
    else:
        print("El archivo todavía no existe.")

else:
    print("Opción no válida.")