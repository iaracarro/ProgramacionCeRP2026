# Desafio 76

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

raiz = Nodo(1)

raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)

raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)

raiz.derecho.izquierodo = Nodo(6)
raiz.derecho.derecho = Nodo(7)

def preorden(nodo):
    if nodo is not None:
        print(nodo.valor)
        preorden(nodo.izquierdo)
        preorden(nodo.derecho)

print("Recorrido en preoden")
preorden(raiz)