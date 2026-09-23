class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.libros = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre != "":
            self.__nombre = nuevo_nombre
        else:
            print("El nombre no puede estar vacío.")

    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        if nueva_nacionalidad != "":
            self.__nacionalidad = nueva_nacionalidad
        else:
            print("La nacionalidad no puede estar vacía.")

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


autor1 = Autor("Julio Verne", "Francés")


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

print()

autor1.nombre = "Julio Gabriel Verne"
autor1.nacionalidad = "Francesa"

print("Datos modificados:")
print("Autor:", autor1.nombre)
print("Nacionalidad:", autor1.nacionalidad)

print()

autor1.nombre = ""
autor1.nacionalidad = ""

print()

print("Datos del autor y sus libros: ")
print("Autor:", autor1.nombre)
print("Nacionalidad:", autor1.nacionalidad)
print()

for libro in autor1.libros:
    print("Título:", libro.titulo)
    print("Género:", libro.genero)
    print("ISBN:", libro.isbn)
    print()
