# Desafio 24

import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Calcular la transpuesta
transpuesta = A.T

# Sumar la matriz con su transpuesta
resultado = A + transpuesta

# Calcular el rango
rango = np.linalg.matrix_rank(resultado)

print("Matriz A + A.T:")
print(resultado)

print("Rango de la matriz:", rango)