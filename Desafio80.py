# Desafio 80

import re

class Nodo:
    def __init__(self, valor):
        self.val = valor
        self.izq = None
        self.der = None

def convertir_postfija(expresion):
    tokens = re.findall(r'\d+|[+\-*/()]', expresion)
    salida = []
    operadores = []

    prioridad = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in tokens:
        if token.isdigit():
            salida.append(token)

        elif token == '(':
            operadores.append(token)

        elif token == ')':
            while operadores and operadores[-1] != '(':
                salida.append(operadores.pop())
            operadores.pop()

        else:
            while (operadores and operadores[-1] != '('
                   and prioridad[operadores[-1]] >= prioridad[token]):
                salida.append(operadores.pop())
            operadores.append(token)

    while operadores:
        salida.append(operadores.pop())

    return salida

def construir_arbol(expresion):
    tokens = convertir_postfija(expresion)
    pila = []

    for token in tokens:
        if token.isdigit():
            pila.append(Nodo(int(token)))
        else:
            nodo = Nodo(token)
            nodo.der = pila.pop()
            nodo.izq = pila.pop()
            pila.append(nodo)

    return pila.pop()

def evaluar(raiz):
    if raiz.val not in ['+', '-', '*', '/']:
        return raiz.val

    izquierda = evaluar(raiz.izq)
    derecha = evaluar(raiz.der)

    if raiz.val == '+':
        return izquierda + derecha
    elif raiz.val == '-':
        return izquierda - derecha
    elif raiz.val == '*':
        return izquierda * derecha
    elif raiz.val == '/':
        return izquierda / derecha

expresion = "5 + 3 * 4"

arbol = construir_arbol(expresion)
resultado = evaluar(arbol)

print("Expresion:", expresion)
print("Resultado:", resultado)