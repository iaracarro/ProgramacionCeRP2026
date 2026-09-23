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


class Poeta(Autor):
    def __init__(self, nombre, nacionalidad, tipo_poesia):
        super().__init__(nombre, nacionalidad)
        self.tipo_poesia = tipo_poesia

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)
        print("Tipo de poesía:", self.tipo_poesia)


poeta1 = Poeta("Pablo Neruda", "Chileno", "Romántica")
poeta2 = Poeta("Mario Benedetti", "Uruguayo", "Social")


poeta1.mostrar_info()
print()

poeta2.mostrar_info()
print()


# Comprobamos que Poeta también puede utilizar métodos heredados de Autor

poeta1.agregar_libro("Veinte poemas de amor y una canción desesperada")
poeta2.agregar_libro("La tregua")

print("Libros de", poeta1.nombre + ":", poeta1.libros)
print("Libros de", poeta2.nombre + ":", poeta2.libros)