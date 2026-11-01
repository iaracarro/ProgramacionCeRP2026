# Desafio 43

def contar_manzanas(manzanas, total=0):
    if manzanas == 0:
        return total

    total += 1

    return contar_manzanas(manzanas - 1, total)


cantidad = int(input("¿Cuántas manzanas tiene la pila? "))

resultado = contar_manzanas(cantidad)

print("El mono contó", resultado, "manzanas.")