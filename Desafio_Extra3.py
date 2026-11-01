# Desafio Extra 3

import math

satelites = {
    "Satélite A": (1, 2, 2),
    "Satélite B": (3, 4, 0),
    "Satélite C": (0, 0, 5),
    "Satélite D": (2, 1, 1),
    "Satélite E": (6, 2, 3)
}

distancias = {}

for nombre, coordenadas in satelites.items():
    x, y, z = coordenadas
    distancia = math.sqrt(x**2 + y**2 + z**2)
    distancias[nombre] = distancia
    print(f"{nombre}: distancia = {distancia:.2f}")

mas_cercano = min(distancias, key=distancias.get)
mas_lejano = max(distancias, key=distancias.get)

print(f"\nSatélite más cercano: {mas_cercano}")
print(f"Satélite más lejano: {mas_lejano}")
