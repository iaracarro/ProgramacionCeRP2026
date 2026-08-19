class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)


class Libro:
    def __init__(self, titulo, genero, isbn):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn


autor1 = Autor("Julio Verne")

libro1 = Libro(
    "Viaje al centro de la Tierra",
    "Aventura",
    "978-1234567890"
)

libro2 = Libro(
    "La vuelta al mundo en 80 días",
    "Aventura",
    "978-0987654321"
)

autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)

print("Autor:", autor1.nombre)

for libro in autor1.libros:
    print("Título:", libro.titulo)
    print("Género:", libro.genero)
    print("ISBN:", libro.isbn)
    print()