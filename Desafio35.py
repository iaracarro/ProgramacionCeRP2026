# Desafio 35

import random
import string

caracteres = string.ascii_letters + string.digits

contrasena = ""

for i in range(8):
    contrasena += random.choice(caracteres)

print("Tu contraseña es:", contrasena)