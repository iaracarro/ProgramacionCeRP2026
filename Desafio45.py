# Desafio 45

class Bilioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        self.libros.append(libro)

    def eliminar(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print("Libro Eliminado.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def buscar(self, libro):
        if libro in self.libros:
            print("El libro se encuentra en la biblioteca.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def mostrar(self):
        print(self.libros)

biblioteca1 = Bilioteca()
biblioteca2 = Bilioteca()

biblioteca1.agregar("El Principito")
biblioteca1.agregar("Planetas a la vista")

biblioteca2.agregar("El Señor de los Anillos")
biblioteca2.agregar("Los Bridgerton")

biblioteca1.eliminar("El Principito")

biblioteca1.buscar("Planetas a la vista")
biblioteca2.buscar("Los Bridgerton")

print("Biblioteca 1:")
biblioteca1.mostrar()

print("Biblioteca 2:")
biblioteca2.mostrar()