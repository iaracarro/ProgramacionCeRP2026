# Desafio 42

def invertir_palabras(palabras, indice=0):
    if indice == len(palabras) - 1:
        return palabras[indice]
    else:
        return invertir_palabras(palabras, indice + 1) + " " + palabras[indice]

oracion = input("Ingrese una oración: ")
palabras = oracion.split()

resultado = invertir_palabras(palabras)

print("Oración Invertida: ", resultado)