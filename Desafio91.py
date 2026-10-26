# Desafio 91

import random

temperaturas = []

for i in range(5):
    temperatura = random.uniform(-10.0, 40.0)
    temperaturas.append(temperatura)

print("Temperaturas generadas:")
print(temperaturas)