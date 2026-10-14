# Desafio 67

try:
    a = int(input("Ingrese el dividendo: "))
    b = int(input("Ingrese el divisor: "))

    resultado = a / b
    print("El resultado es:", resultado)

except ZeroDivisionError:
    print("Error: División por cero no permitida.")

except ValueError:
    print("Error: Debe ingresar números enteros.")