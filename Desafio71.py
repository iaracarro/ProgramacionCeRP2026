# Desafio 71

archivo = None

try:
    archivo = open("mi_archivo.txt", "r", encoding="utf-8")
    contenido = archivo.read()
    print(contenido)

except FileNotFoundError:
    print("Error: el archivo no existe.")

except OSError as error:
    print(f"Error al leer el archivo: {error}")

finally:
    if archivo is not None:
        archivo.close()
        print("El archivo se cerró correctamente.")