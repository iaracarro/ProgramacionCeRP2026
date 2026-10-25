# Desafio 78

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

def encontrar_maximo(raiz):
    if raiz is None:
        return float("-inf")

    izquierda = encontrar_maximo(raiz.izq)
    derecha = encontrar_maximo(raiz.der)

    return max(izquierda, derecha, raiz.val)

resultado = encontrar_maximo(raiz)
print("El valor maximo es:", resultado)