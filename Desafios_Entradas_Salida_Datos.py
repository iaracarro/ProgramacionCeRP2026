# Desafio 1: Escriba un programa que pida al usuario su nombre y su ciudad de origen, luego imprima un saludo personalizado con esa información.

nombre = input("Ingrese su nombre: ")
ciudad = input("Ingrese su ciudad de origen: ")

print(f"Hola {nombre}, ¡qué lindo saludarte desde {ciudad}!")

# ------------------------------------------------------------------------------

# Desafio 2: Escriba un programa que pida al usuario que ingrese dos números y luego imprima la suma, la resta, la multiplicación y la división de esos números.

numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)
print("Division:", division)

# -----------------------------------------------------------------------------

# Desafio 3: Escriba un programa que pueda tomar los detalles de los productos (nombre, cantidad, precio) y produzca una factura bien formateada.

producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad: "))
precio = float(input("Ingrese el precio unitario: "))

total = cantidad * precio

print("\n--------- FACTURA ---------")
print("Producto:", producto)
print("Cantidad:", cantidad)
print(f"Precio unitario: ${precio:.2f}")
print(f"Total a pagar: ${total:.2f}")
print("---------------------------")

# -------------------------------------------------------------------------------

# Problemas:

fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print(f"{fahrenheit} grados Fahrenheit equivalen a {celsius:.2f} grados Celsius.")

# -------------------------------------------------------------------------------------

# Problema 2

peso = input("Ingrese su peso en kilogramos: ")
peso = float(peso)

altura = input("Ingrese su altura en metros: ")
altura = float(altura)

imc = peso / altura**2

print(f"Su Indice de Masa Corporal es {imc:.2f}.")

# ------------------------------------------------------------------------------------------

# Problema 3

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

anio_nacimiento = input("Ingrese su año de nacimiento: ")
anio_nacimiento = int(anio_nacimiento)

anio_actual = input("Ingrese el año actual: ")
anio_actual = int(anio_actual)

edad = anio_actual - anio_nacimiento

print(f"Nombre: {nombre}\nApellido: {apellido}\nEdad aproximada: {edad} años.")

# -----------------------------------------------------------------------------------------------

# Problema 4

import csv

suma = 0
cantidad = 0

with open("calificaciones.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        nota = float(fila["calificacion"])
        suma += nota
        cantidad += 1

promedio = suma / cantidad

with open("promedio.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Promedio"])
    escritor.writerow([promedio])

print("El promedio es:", promedio)
print("El resultado se guardó en promedio.csv")

# ----------------------------------------------------------------------------------------------------------------------------

# Problema 5

import json

with open("calificaciones.json", "r", encoding="utf-8") as archivo:
    estudiantes = json.load(archivo)

suma_total = 0
contador = 0

for estudiante in estudiantes:
    suma_total += estudiante["calificacion"]
    contador += 1

promedio = suma_total / contador if contador > 0 else 0

with open("promedio_calificaciones.json", "w", encoding="utf-8") as archivo:
    json.dump({"promedio_calificaciones": promedio}, archivo, indent=4)

print("El promedio es:", promedio)

# -----------------------------------------------------------------------------------------------------------------

# Problema 6

import requests

respuesta = requests.get(
    "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
)

datos = respuesta.json()

precio_bitcoin = datos["bpi"]["USD"]["rate"]

print(f"El precio actual de Bitcoin es: {precio_bitcoin} USD")

# ------------------------------------------------------------------------------------------------------------------

# Problema 7

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("calificaciones.csv")

promedio = df["Calificacion"].mean()

print(f"El promedio de las calificaciones es: {promedio}")

bins = [i - 0.5 for i in range(2, 12)]

plt.hist(df["Calificacion"], bins=bins, edgecolor="black")

plt.title("Distribución de las Calificaciones")
plt.xlabel("Calificaciones")
plt.ylabel("Cantidad de Estudiantes")
plt.xticks(range(1, 11))

plt.show()

# ----------------------------------------------------------------------------------------------

# Problema 8

df_agrupado = df.groupby("Nombre")["Calificacion"].mean().reset_index()

plt.figure(figsize=(10, 6))

plt.bar(
    df_agrupado["Nombre"],
    df_agrupado["Calificacion"],
    color="skyblue"
)

plt.title("Promedio de Calificaciones por Estudiante")
plt.xlabel("Estudiantes")
plt.ylabel("Promedio de Calificaciones")
plt.xticks(rotation=45)

plt.show()