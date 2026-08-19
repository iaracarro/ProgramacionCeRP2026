def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

print("El MCD es:", mcd(numero1, numero2))