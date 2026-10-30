# Desafio 50

class Autor:
    def __init__(self, nombre="", nacionalidad=""):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = ""
        self.libros_publicados = []

    def agregar_libro(self, libro):
        self.libros_publicados.append(libro)

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)
        print("Fecha de nacimiento:", self.fecha_nacimiento)
        print("Libros publicados:", self.libros_publicados)


# Crear autor
autor1 = Autor("Mario Benedetti", "Uruguaya")

# Agregar información
autor1.fecha_nacimiento = "1920"
autor1.agregar_libro("La tregua")
autor1.agregar_libro("Gracias por el fuego")

# Mostrar información
autor1.mostrar_datos()