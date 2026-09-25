class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn


class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo):
        super().__init__(titulo, autor, isbn)
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

    def mostrar_informacion(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("ISBN:", self.isbn)
        print("Formato:", self.formato)
        print("Tamaño del archivo:", self.tamaño_archivo)


class EBook(LibroDigital):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo, enlace_descarga):
        super().__init__(titulo, autor, isbn, formato, tamaño_archivo)
        self.enlace_descarga = enlace_descarga

    def mostrar_informacion(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("ISBN:", self.isbn)
        print("Formato:", self.formato)
        print("Tamaño del archivo:", self.tamaño_archivo)
        print("Enlace de descarga:", self.enlace_descarga)


libro_digital = LibroDigital(
    "Viaje al centro de la Tierra",
    "Julio Verne",
    "978-1234567890",
    "PDF",
    "5 MB"
)

ebook = EBook(
    "La vuelta al mundo en 80 días",
    "Julio Verne",
    "978-0987654321",
    "EPUB",
    "3 MB",
    "https://biblioteca.com/ebook"
)


print("INFORMACIÓN DEL LIBRO DIGITAL")
libro_digital.mostrar_informacion()

print()

print("INFORMACIÓN DEL EBOOK")
ebook.mostrar_informacion()