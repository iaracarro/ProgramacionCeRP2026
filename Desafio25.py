# Desafio 25

import random

# tablero de 5 filas y 5 columnas
tablero = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# posicion aleatoria de 3 barcos
for i in range(3):
    while True:

        # fila y una columna aleatorias.
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)

        if tablero[fila][columna] == 0:
            tablero[fila][columna] = 1
            break

# 'X' son las filas, 'Y' son las columnas
def disparo(x, y):

    if tablero[x][y] == 1:
        print("¡Barco golpeado!")
    else:
        print("Agua.")

# Mostramos el tablero.
print("Tablero:")
for fila in tablero:
    print(fila)

# el usuario da las coordenadas del disparo.
x = int(input("Ingrese la fila (0 a 4): "))
y = int(input("Ingrese la columna (0 a 4): "))

# Ejecutamos la función del disparo.
disparo(x, y)