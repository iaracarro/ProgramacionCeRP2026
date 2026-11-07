# Desafio 1:

aprobados = 0
desaprobados = 0

while True:
    calificacion = int(input("Ingrese una calificación (0 para terminar): "))

    if calificacion == 0:
        break

    if calificacion >= 7:
        aprobados += 1
    else:
        desaprobados += 1

print(f"Cantidad de aprobados: {aprobados}")
print(f"Cantidad de desaprobados: {desaprobados}")

# .............................................................................................................................

# Desafio 2:

calificaciones = input("Ingrese las calificaciones separadas por comas: ")

lista_calificaciones = calificaciones.split(",")

suma = 0

for nota in lista_calificaciones:
    suma += float(nota)

promedio = suma / len(lista_calificaciones)

print(f"El promedio de las calificaciones es: {promedio:.2f}")

# --------------------------------------------------------------------------------------------------------------------------------

# Desafio 3:

import random

autos = ["Auto 1", "Auto 2", "Auto 3"]

distancias = [0, 0, 0]

velocidades = [
    random.randint(1, 10),
    random.randint(1, 10),
    random.randint(1, 10)
]

for segundo in range(10):
    for i in range(len(autos)):
        distancias[i] += velocidades[i]

print("Distancias finales:")

for i in range(len(autos)):
    print(f"{autos[i]}: {distancias[i]} metros")

mayor_distancia = max(distancias)

print("\nGanador/es:")

for i in range(len(autos)):
    if distancias[i] == mayor_distancia:
        print(autos[i])

# ------------------------------------------------------------------------------------------------------------------------------

# Problema 1:

import numpy as np

conceptos_gastos = np.array([
    "Transporte",
    "Alojamiento",
    "Alimentación",
    "Actividades",
    "Otros"
])

total_gastos = 0

for concepto in conceptos_gastos:
    costo = float(input(f"Ingrese el costo estimado para {concepto}: "))
    total_gastos += costo

print(f"El total de gastos estimados para el viaje es: {total_gastos}")

# -------------------------------------------------------------------------------------------------------------------------------

# Problema 2:

import pandas as pd

df = pd.read_csv("calificaciones.csv")

total_calificaciones = 0
numero_calificaciones = 0

for index, row in df.iterrows():
    nombre = row['Nombre']
    calificacion = int(row['Calificacion'])
    total_calificaciones += calificacion
    numero_calificaciones += 1
    print(f"La calificación de {nombre} es: {calificacion}")

promedio_general = total_calificaciones / numero_calificaciones
print(f"El promedio general de las calificaciones es: {promedio_general:.2f}")