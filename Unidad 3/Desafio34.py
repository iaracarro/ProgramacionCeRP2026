# Desafio 34

import string

texto = input("Ingrese un texto: ")

texto_mayusculas = string.capwords(texto)

letras = string.ascii_lowercase

signos = string.punctuation

print("Texto corregido:", texto_mayusculas)
print("Letras del alfabeto:", letras)
print("Signos de puntuacion:", signos)