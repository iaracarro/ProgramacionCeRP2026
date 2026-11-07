# Desafio 30

def calcular_mcd(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto

    return a

numero1 = 48
numero2 = 18

resultado = calcular_mcd(numero1, numero2)

print("El MCD es:", resultado)