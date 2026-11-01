# Desafio 41

import procesador_texto

def resaltar_recursivo(texto, palabra, indice=0):
    palabras = texto.split()

    if indice >= len(palabras):
        return []

    if palabras[indice] == palabra:
        actual = procesador_texto.negrita(palabras[indice])
    else:
        actual = palabras[indice]

    # Seguimos con la siguiente palabra
    resto = resaltar_recursivo(texto, palabra, indice + 1)

    return [actual] + resto


texto = "el ingrediente principal es harina y otro ingrediente es agua"
resultado = resaltar_recursivo(texto, "ingrediente")

print(" ".join(resultado))