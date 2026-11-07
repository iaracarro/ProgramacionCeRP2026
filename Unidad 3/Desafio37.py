# Desafio 37

from collections import Counter
import matplotlib.pyplot as plt
import string

texto = input("Ingrese un texto: ").lower()

texto = texto.translate(str.maketrans("", "", string.punctuation))

palabras = texto.split()

frecuencias = Counter(palabras)

mas_comunes = frecuencias.most_common(10)

for palabra, cantidad in mas_comunes:
    print(palabra, ":", cantidad)

if mas_comunes:
    nombres = [palabra for palabra, cantidad in mas_comunes]
    cantidades = [cantidad for palabra, cantidad in mas_comunes]

    plt.bar(nombres, cantidades)
    plt.xlabel("Palabras")
    plt.ylabel("Frecuencia")
    plt.title("Las 10 palabras más comunes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()