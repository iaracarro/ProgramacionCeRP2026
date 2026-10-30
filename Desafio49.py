# Desafio 49

class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad


class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


class Biblioteca:
    def __init__(self):
        self.autores = []
        self.libros = []

    def agregar_autor(self, autor):
        self.autores.append(autor)

    def agregar_libro(self, libro):
        self.libros.append(libro)


# Crear biblioteca
biblioteca = Biblioteca()

# Crear autores
autor1 = Autor("Mario Benedetti", "Uruguaya")
autor2 = Autor("Gabriel García Márquez", "Colombiana")

# Agregar autores
biblioteca.agregar_autor(autor1)
biblioteca.agregar_autor(autor2)

# Crear libros
libro1 = Libro("La tregua", autor1)
libro2 = Libro("Cien años de soledad", autor2)

# Agregar libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Mostrar libros
for libro in biblioteca.libros:
    print(libro.titulo, "-", libro.autor.nombre)