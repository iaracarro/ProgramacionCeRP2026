# Desafio 68

valores = [10, 0, "hola", 5, None, "8"]

for valor in valores:
    try:
        numero = float(valor)
        resultado = 100 / numero
        print(f"El resultado de 100 / {numero} es {resultado}")

    except ZeroDivisionError:
        print(f"Error: no se puede dividir entre cero ({valor}).")

    except TypeError:
        print(f"Error: el valor {valor} tiene un tipo de dato incorrecto.")

    except ValueError:
        print(f"Error: no se puede convertir {valor} en un número.")