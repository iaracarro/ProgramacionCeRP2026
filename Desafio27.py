# Desafio 27

def calcular_suma_promedio(numeros):
    suma = sum(numeros)
    promedio = suma / len(numeros)
    return suma, promedio


lista = [4, 6, 8, 10]

suma, promedio = calcular_suma_promedio(lista)

print("La suma es:", suma)
print("El promedio es:", promedio)