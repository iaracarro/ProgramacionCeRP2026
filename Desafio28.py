# Desafio 28

def poner_mayusculas(texto):
    resultado = texto.title()
    return resultado

frase = input("ingrese una frase: ")

nueva_frase = poner_mayusculas(frase)

print(nueva_frase)