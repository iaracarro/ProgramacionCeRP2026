# Desafio 58

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre


class Bibliotecario(Usuario):
    def __init__(self, nombre, seccion, años_experiencia):
        super().__init__(nombre)
        self.seccion = seccion
        self.años_experiencia = años_experiencia

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Sección:", self.seccion)
        print("Años de experiencia:", self.años_experiencia)


bibliotecario1 = Bibliotecario(
    "Carlos Pérez",
    "Literatura",
    5
)

bibliotecario1.mostrar_datos()