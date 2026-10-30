# Desafio 63

class Autor:
    def __init__(self, nombre):
        self.nombre = nombre

    def biografia(self):
        return "El autor se llama " + self.nombre


class Escritor(Autor):
    def __init__(self, nombre, genero):
        super().__init__(nombre)
        self.genero = genero

    def biografia(self):
        return super().biografia() + " y escribe " + self.genero


escritor1 = Escritor("Mario Benedetti", "Realismo Social")

print("Biografía completa:")
print(escritor1.biografia())

print()
print("Biografía de la clase Autor:")
print(Autor.biografia(escritor1))