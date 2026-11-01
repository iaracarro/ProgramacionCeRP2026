# Desafio 31

def es_palindromo(texto):
    texto = texto.lower()
    if texto == texto[::-1]:
        return True
    else:
        return False

palabra = input("Ingrese una palabra: ")

print(es_palindromo(palabra))