# Desafio 88

import csv

libro_buscado = input("Ingrese el nombre del libro: ")
nueva_cantidad = input("Ingrese la nueva cantidad de copias: ")

with open("inventario.csv", "r", newline="", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    filas = list(lector)

encontrado = False

for fila in filas[1:]:
    if fila[0].strip().lower() == libro_buscado.strip().lower():
        fila[1] = nueva_cantidad
        encontrado = True
        break

if encontrado:
    with open("inventario.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(filas)

    print("Inventario actualizado correctamente.")
else:
    print("No se encontró ese libro en el inventario.")