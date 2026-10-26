# Desafio 90

import re

def contar_palabras(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            texto = archivo.read().lower()

        palabras = re.findall(r"\b\w+\b", texto)
        conteo = {}

        for palabra in palabras:
            if palabra in conteo:
                conteo[palabra] += 1
            else:
                conteo[palabra] = 1

        palabras_comunes = sorted(
            conteo.items(),
            key=lambda elemento: elemento[1],
            reverse=True
        )

        print("Las 5 palabras más comunes son:")

        for palabra, cantidad in palabras_comunes[:5]:
            print(f"{palabra}: {cantidad} veces")

    except FileNotFoundError:
        print("No se encontró el archivo:", nombre_archivo)


contar_palabras("libros.txt")