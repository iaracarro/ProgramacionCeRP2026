# Desafio 23

import numpy as np

A = np.array([
    [1, 0, 1],
    [4, -1, 4],
    [5, 6, 7]
])

# Calcular la matriz inversa
inversa = np.linalg.inv(A)

# Calcular la traza de la inversa
traza = np.trace(inversa)

print("Matriz inversa:")
print(inversa)

print("Traza de la matriz inversa:", traza)