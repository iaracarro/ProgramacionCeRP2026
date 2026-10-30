# Desafio 66

class Operacion:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def resultado(self):
        pass


class Suma(Operacion):
    def resultado(self):
        return self.numero1 + self.numero2


class Multiplicacion(Operacion):
    def resultado(self):
        return self.numero1 * self.numero2

suma1 = Suma(10, 5)
multiplicacion1 = Multiplicacion(10, 5)

print("Resultado de la suma:", suma1.resultado())
print("Resultado de la multiplicación:", multiplicacion1.resultado())