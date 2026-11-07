# Desafio Extra 2

import random

caras = [1, 2, 3, 4, 5, 6]

dados = random.choices(caras, k=2)

print("Resultado del primer dado:", dados[0])
print("Resultado del segundo dado:", dados[1])
print("Suma de los dados:", sum(dados))