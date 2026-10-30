# Desafio53

class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)


class Libro:
    def __init__(self, titulo):
        self.titulo = titulo


autor1 = Autor("Julio Verne")

libro1 = Libro("Viaje al centro de la Tierra")
libro2 = Libro("La vuelta al mundo en 80 días")

autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)

print("Autor:", autor1.nombre)
print("Libros publicados:")

for libro in autor1.libros:
    print(libro.titulo)