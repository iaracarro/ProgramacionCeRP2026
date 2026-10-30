# Desafio 60

class Autor:
    def __init__(self, nombre, **kwargs):
        self.nombre = nombre
        super().__init__(**kwargs)

class Escritor(Autor):
    def __init__(self, nombre, genero, **kwargs):
        self.genero = genero
        super().__init__(nombre=nombre, **kwargs)

class Academico:
    def __init__(self, universidad, **kwargs):
        self.universidad = universidad
        super().__init__(**kwargs)

class EscritorAcademico(Escritor, Academico):
    def __init__(self, nombre, genero, universidad):
        super().__init__(
            nombre=nombre,
            genero=genero,
            universidad=universidad
        )

    def publicar_articulo(self, articulo):
        print("Artículo académico publicado:", articulo)

escritor1 = EscritorAcademico(
    "Mario Benedetti",
    "Literatura",
    "Universidad de la República"
)

print("Nombre:", escritor1.nombre)
print("Género:", escritor1.genero)
print("Universidad:", escritor1.universidad)

escritor1.publicar_articulo("La literatura uruguaya")