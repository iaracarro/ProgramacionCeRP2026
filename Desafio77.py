# Desafio 77

class Nodo:
    def __init__(self, valor):
        self.izq = None
        self.der = None
        self.val = valor

raiz = Nodo(1)

raiz.izq = Nodo(2)
raiz.der = Nodo(3)

raiz.izq.izq = Nodo(4)
raiz.izq.der = Nodo(5)

raiz.der.izq = Nodo(6)
raiz.der.der = Nodo(7)

def sumar_inorden(raiz):
    if raiz is None:
        return 0

    izquierda = sumar_inorden(raiz.izq)
    derecha = sumar_inorden(raiz.der)

    return izquierda + raiz.val + derecha

resultado = sumar_inorden(raiz)
print("La suma de los valores es:", resultado)