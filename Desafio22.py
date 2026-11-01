# Desafio 22

import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

# Multiplicar A por 2
dos_A = 2 * A

# Calcular la transpuesta de B
B_transpuesta = B.T

# Sumar ambas matrices
resultado = dos_A + B_transpuesta

print("Matriz 2A:")
print(dos_A)

print("Matriz B transpuesta:")
print(B_transpuesta)

print("Resultado de 2A + B.T:")
print(resultado)