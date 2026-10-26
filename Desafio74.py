# Desafio 74

lista1 = [10, 20, 30, 40]
lista2 = [1, 2]

resultado = []

for i in range(max(len(lista1), len(lista2))):
    num1 = lista1[i] if i < len(lista1) else 0
    num2 = lista2[i] if i < len(lista2) else 0

    resultado.append(num1 + num2)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Suma:", resultado)