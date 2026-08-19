# Desafío 3: Suma de los primeros n números naturales

n = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(1, n + 1):
    suma = suma + i

# resultado
print("La suma de los primeros", n, "números naturales es:", suma)