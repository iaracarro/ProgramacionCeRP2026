#Desafio 17: Carera de Autos

import random

# Velocidad aleatoria
velocidad1 = random.randint(10, 20)
velocidad2 = random.randint(10, 20) 
velocidad3 = random.randint(10, 20)

# Distancia inicial
distancia1 = 0
distancia2 = 0
distancia3 = 0

# Carrera de 10 segundos
for segundo in range(10):
    distancia1 += velocidad1
    distancia2 += velocidad2
    distancia3 += velocidad3

# mostrar resultados
print(f"Auto 1: {distancia1} metros")
print(f"Auto 2: {distancia2} metros")
print(f"Auto 3: {distancia3} metros")

# buscar la distancia maxima
maxima =max(distancia1, distancia2, distancia3)

print("El ganador es:")

if distancia1 == maxima:
    print("Auto 1")


if distancia2 == maxima:
    print("Auto 2")

if distancia3 == maxima:
    print("Auto 3")