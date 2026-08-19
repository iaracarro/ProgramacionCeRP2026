# Solicita un texto al usuario
texto = input("Ingrese un texto: ")

# Divide el texto en palabras
palabras = texto.split()

# Cuenta la cantidad de palabras
cantidad = len(palabras)

# Muestra el resultado
print(f"El texto contiene {cantidad} palabras.")