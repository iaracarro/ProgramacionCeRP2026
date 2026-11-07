# Desafio 8: Analicis de Texto

import re

texto = """
Python es un lenguaje de programación.
Python permite aprender programación de manera práctica.
Aprender Python puede ser divertido.
"""

# Extraer las palabras e ignorar mayúsculas y minúsculas
palabras = re.findall(r"\b\w+\b", texto.lower())

# Crear un conjunto para quedarnos con palabras únicas
palabras_unicas = set(palabras)

print("Cantidad de palabras únicas:", len(palabras_unicas))

# Ordenar por longitud
palabras_ordenadas = sorted(palabras_unicas, key=len)

print("\nLas 10 palabras más cortas:")
print(palabras_ordenadas[:10])

print("\nLas 10 palabras más largas:")
print(palabras_ordenadas[-10:][::-1])