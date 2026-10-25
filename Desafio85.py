# Desafio 84

class Nodo:
    def __init__(self, nombre, promedio):
        self.nombre = nombre
        self.promedio = promedio
        self.izq = None
        self.der = None


def insertar(raiz, nombre, promedio):
    if raiz is None:
        return Nodo(nombre, promedio)

    if promedio < raiz.promedio:
        raiz.izq = insertar(raiz.izq, nombre, promedio)
    else:
        raiz.der = insertar(raiz.der, nombre, promedio)

    return raiz


def recorrer_en_orden(raiz):
    if raiz is not None:
        recorrer_en_orden(raiz.izq)
        print(raiz.nombre, "-", raiz.promedio)
        recorrer_en_orden(raiz.der)


estudiantes = [
    ("Ana", 8.5),
    ("Luis", 6.5),
    ("Sofía", 9.2),
    ("Bruno", 7.8)
]

raiz = None

for nombre, promedio in estudiantes:
    raiz = insertar(raiz, nombre, promedio)

recorrer_en_orden(raiz)