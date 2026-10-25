# Desafio 79

class Nodo:
    def __init__(self, valor):
        self.val = valor
        self.izq = None
        self.der = None

def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)

    if valor < raiz.val:
        raiz.izq = insertar(raiz.izq, valor)
    elif valor > raiz.val:
        raiz.der = insertar(raiz.der, valor)

    return raiz

def buscar(raiz, valor):
    if raiz is None:
        return False

    if raiz.val == valor:
        return True
    elif valor < raiz.val:
        return buscar(raiz.izq, valor)
    else:
        return buscar(raiz.der, valor)

numeros = [8, 4, 12, 2, 6, 10, 14]
raiz = None

for numero in numeros:
    raiz = insertar(raiz, numero)

print("¿Esta el numero 10?", buscar(raiz, 10))
print("¿Esta el numero 5?", buscar(raiz, 5))