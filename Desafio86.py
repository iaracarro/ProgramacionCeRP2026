# Desafío 86

libro = input("Ingrese el nombre del libro: ")
prestatario = input("Ingrese el nombre del prestatario: ")
fecha = input("Ingrese la fecha del préstamo: ")

with open("prestamos.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{libro},{prestatario},{fecha}\n")

print("Préstamo registrado correctamente.")