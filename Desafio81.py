# Desafio 81

from collections import deque

class Nodo:
    def __init__(self, grado, estudiantes):
        self.grado = grado
        self.estudiantes = estudiantes
        self.izq = None
        self.der = None

def recorrido_por_niveles(raiz):
    if raiz is None:
        return

    cola = deque([raiz])

    while cola:
        nodo = cola.popleft()
        print(f"Grado {nodo.grado}: {nodo.estudiantes}")

        if nodo.izq:
            cola.append(nodo.izq)

        if nodo.der:
            cola.append(nodo.der)

# Crear el árbol
raiz = Nodo(12, ["Ana", "Luis"])
raiz.izq = Nodo(11, ["Sofía", "Juan"])
raiz.der = Nodo(10, ["Pedro", "Emma"])
raiz.izq.izq = Nodo(9, ["Mía", "Tomás"])
raiz.izq.der = Nodo(8, ["Noa", "Leo"])

# Recorrer el árbol
recorrido_por_niveles(raiz)