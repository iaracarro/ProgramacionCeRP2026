#Desafio 47

class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)


autor1 = Autor("Julio Verne")

autor1.agregar_libro("Viaje al centro de la Tierra")
autor1.agregar_libro("La vuelta al mundo en 80 días")
autor1.agregar_libro("Veinte mil leguas de viaje submarino")

print("Autor:", autor1.nombre)
print("Libros:", autor1.libros)

autor1.eliminar_libro("La vuelta al mundo en 80 días")

print("Después de eliminar:")
print("Libros:", autor1.libros)