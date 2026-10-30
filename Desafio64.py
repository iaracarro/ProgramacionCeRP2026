# Desafio 64

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo_estudio, nivel):
        super().__init__(titulo, autor)
        self.campo_estudio = campo_estudio
        self.nivel = nivel


libro1 = LibroEspecializado(
    "Programación en Python",
    "Juan Pérez",
    "Informática",
    "Avanzado"
)

print("Título:", libro1.titulo)
print("Autor:", libro1.autor)
print("Campo de estudio:", libro1.campo_estudio)
print("Nivel:", libro1.nivel)