# Desafío 4: Cantidad de números pares en una lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
contador = 0
for num in numeros:
    if num % 2 == 0:   
        contador = contador + 1

# resultado
print("Cantidad de números pares:", contador)