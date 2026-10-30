# Desafo 55

class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)


class Libro:
    def __init__(self, titulo):
        self.titulo = titulo


def obtener_titulos(autor):
    titulos = []

    for libro in autor.libros:
        titulos.append(libro.titulo)

    return titulos


autor1 = Autor("Julio Verne")

libro1 = Libro("Viaje al centro de la Tierra")
libro2 = Libro("La vuelta al mundo en 80 días")
libro3 = Libro("Veinte mil leguas de viaje submarino")

autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)
autor1.agregar_libro(libro3)

print("Libros de", autor1.nombre)
print(obtener_titulos(autor1))