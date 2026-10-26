# Desafio 72

codigos = [120, 245, 378, 492, 516]

codigo_buscado = int(input("Ingresá el código del producto: "))

if codigo_buscado in codigos:
    posicion = codigos.index(codigo_buscado)
    print(f"El código está en la posición {posicion}.")
else:
    print("El código no se encontró.")