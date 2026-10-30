# Desafio 56

class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)


class Libro:
    def __init__(self, titulo):
        self.titulo = titulo


def autor_mas_libros(autores):
    if len(autores) == 0:
        return None

    mayor = autores[0]

    for autor in autores:
        if len(autor.libros) > len(mayor.libros):
            mayor = autor

    return mayor

autor1 = Autor("Julio Verne")
autor2 = Autor("Mario Benedetti")
autor3 = Autor("Gabriel García Márquez")

libro1 = Libro("Viaje al centro de la Tierra")
libro2 = Libro("La vuelta al mundo en 80 días")
libro3 = Libro("Veinte mil leguas de viaje submarino")
libro4 = Libro("La tregua")
libro5 = Libro("Gracias por el fuego")

autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)
autor1.agregar_libro(libro3)

autor2.agregar_libro(libro4)
autor2.agregar_libro(libro5)

autores = [autor1, autor2, autor3]

resultado = autor_mas_libros(autores)

if resultado != None:
    print("Autor con más libros:", resultado.nombre)
    print("Cantidad de libros:", len(resultado.libros))
else:
    print("No hay autores registrados.")