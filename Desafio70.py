# Desafio 70

import math

class NegativeNumberError(Exception):
    pass

try:
    numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))

    if numero < 0:
        raise NegativeNumberError("No se puede calcular la raíz cuadrada de un número negativo.")

    resultado = math.sqrt(numero)
    print("La raíz cuadrada es:", resultado)

except NegativeNumberError as error:
    print("Error:", error)

except ValueError:
    print("Error: Debe ingresar un número válido.")