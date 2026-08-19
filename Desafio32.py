# Desafio 32: Verificación y cálculo de números primos

def es_primo(numero):
    # Los números menores que 2 no son primos
    if numero < 2:
        return False

    # Comprobamos divisores desde 2 hasta numero - 1
    for i in range(2, numero):

        # Si es divisible, no es primo
        if numero % i == 0:
            return False
    return True

def contar_primos(lista):
    cantidad = 0

    for numero in lista:

        # Si es primo, se aumenta el contador
        if es_primo(numero):
            cantidad += 1
    return cantidad


def main():
    numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print("Cantidad de primos:", contar_primos(numeros))

main()