class Figura:
    def area(self):
        return 0

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.1416 * self.radio ** 2

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2

circulo = Circulo(5)
cuadrado = Cuadrado(4)

figuras = [circulo, cuadrado]

for figura in figuras:
    print("Figura:", figura.__class__.__name__)
    print("Área:", figura.area())