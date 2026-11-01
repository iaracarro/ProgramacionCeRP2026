# Desafio 26

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Crear el tablero de 10 x 10
def crear_tablero(n, m):
    tablero = np.zeros((n, m), dtype=int)

    # Patrón inicial
    tablero[1, 2] = 1
    tablero[2, 3] = 1
    tablero[3, 1] = 1
    tablero[3, 2] = 1
    tablero[3, 3] = 1

    return tablero


# Contar los vecinos vivos de una celda
def contar_vecinos(tablero, fila, columna):
    filas, columnas = tablero.shape
    vecinos = 0

    for i in range(max(0, fila - 1), min(filas, fila + 2)):
        for j in range(max(0, columna - 1), min(columnas, columna + 2)):
            if i == fila and j == columna:
                continue
            vecinos += tablero[i, j]

    return vecinos


# Actualizar el tablero según las reglas
def actualizar_tablero(tablero):
    filas, columnas = tablero.shape
    nuevo = np.zeros((filas, columnas), dtype=int)

    for i in range(filas):
        for j in range(columnas):
            vecinos = contar_vecinos(tablero, i, j)

            if tablero[i, j] == 1:
                if vecinos == 2 or vecinos == 3:
                    nuevo[i, j] = 1
            else:
                if vecinos == 3:
                    nuevo[i, j] = 1

    return nuevo


# Crear el tablero inicial
tablero = crear_tablero(10, 10)

# Mostrar la evolución
fig, ax = plt.subplots()

imagen = ax.imshow(tablero, cmap="binary")
ax.set_title("Juego de la vida de Conway")
ax.set_xticks(range(10))
ax.set_yticks(range(10))
ax.grid(True)

def animar(frame):
    global tablero
    tablero = actualizar_tablero(tablero)
    imagen.set_data(tablero)
    return [imagen]

animacion = FuncAnimation(
    fig, animar, frames=20, interval=500, blit=True
)

plt.show()