# Desafio 29

def tienen_comun(lista1, lista2):
    for elemento in lista1:
        if elemento in lista2:
            return True

    return False


numeros1 = input("Ingrese cuatro numeros: ")
numeros2 = input("Ingrese cuatro numeros: ")

lista1 = numeros1.split(",")
lista2 = numeros2.split(",")

print(tienen_comun(lista1, lista2))