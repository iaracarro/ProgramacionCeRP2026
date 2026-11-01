# Desafio Extra 1

num1 = int(input("Ingresá el primer número entero: "))
num2 = int(input("Ingresá el segundo número entero: "))
num3 = int(input("Ingresá el tercer número entero: "))

if num1 == num2 == num3:
    print("Los tres números son iguales.")
else:
    mayor = max(num1, num2, num3)
    print(f"El número mayor es {mayor}.")