# Desafio 89

try:
    with open("prestamos.txt", "r", encoding="utf-8") as archivo:
        prestamos = archivo.readlines()

    if not prestamos:
        print("No hay prestamos registrados.")

    else:
        print("Registros actuales de prestamos:")

        for numero, prestamo in enumerate(prestamos, start=1):
            print(f"{numero}. {prestamo.strip()}")

        seleccion = int(input("Ingrese el numero del prestamo que desea eliminar: "))

        if 1 <= seleccion <= len(prestamos):
            eliminado = prestamos.pop(seleccion - 1)

            with open("prestamos.txt", "w", encoding="utf-8") as archivo:
                archivo.writelines(prestamos)

            print("Prestamo eliminado correctamente.")
            print("Registro eliminado:", eliminado.strip())

        else:
            print("Numero de prestamo invalido.")

except FileNotFoundError:
    print("No se encontro el archivo prestamos.txt.")

except ValueError:
    print("Debe ingresar un numero entero.")