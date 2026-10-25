# Desafio 73

numeros = [1, 2, 3, 2, 4, 1, 5, 3]

sin_duplicados = []

for numero in numeros:
    if numero not in sin_duplicados:
        sin_duplicados.append(numero)

print("Lista original:", numeros)
print("Lista sin duplicados:", sin_duplicados)