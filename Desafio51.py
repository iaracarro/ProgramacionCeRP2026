# Desafio 51

class Autor:
    def __init__(self, nombre):
        self.nombre = nombre


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

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                print("Libro encontrado:", libro.titulo)
                print("Autor:", libro.autor.nombre)
                return

        print("Libro no encontrado.")

    def buscar_autor(self, nombre):
        for autor in self.autores:
            if autor.nombre.lower() == nombre.lower():
                print("Autor encontrado:", autor.nombre)
                return

        print("Autor no encontrado.")


# Crear biblioteca
biblioteca = Biblioteca()

# Crear autores
autor1 = Autor("Mario Benedetti")
autor2 = Autor("Gabriel García Márquez")

biblioteca.agregar_autor(autor1)
biblioteca.agregar_autor(autor2)

# Crear libros
libro1 = Libro("La tregua", autor1)
libro2 = Libro("Cien años de soledad", autor2)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Buscar información
biblioteca.buscar_libro("La tregua")
biblioteca.buscar_autor("Mario Benedetti")