# Desafio 52

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    # Métodos getter
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_isbn(self):
        return self.__isbn

    # Métodos setter
    def set_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    def set_isbn(self, nuevo_isbn):
        self.__isbn = nuevo_isbn


# Crear un libro
libro1 = Libro(
    "Viaje al centro de la Tierra",
    "Julio Verne",
    "978-1234567890"
)

# Mostrar información del libro
print("Datos del libro:")
print("Título:", libro1.get_titulo())
print("Autor:", libro1.get_autor())
print("ISBN:", libro1.get_isbn())

# Modificar información
libro1.set_titulo("La vuelta al mundo en 80 días")

print()
print("Título modificado:", libro1.get_titulo())