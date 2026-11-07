# Desafio 69

import math

def calcular_factorial(numero):
    try:
        if not isinstance(numero, int):
            raise TypeError("El número debe ser entero.")

        if numero < 0:
            raise ValueError("El número no puede ser negativo.")

        if numero > 1000:
            raise OverflowError("El número es demasiado grande.")

        return math.factorial(numero)

    except (TypeError, ValueError, OverflowError) as error:
        print(f"Error: {error}")
        return None


print(calcular_factorial(5))
print(calcular_factorial(-3))
print(calcular_factorial(2.5))
print(calcular_factorial(1001))