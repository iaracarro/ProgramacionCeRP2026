#Desafio 7: Conversion de Temperatura

#Pedir temperatura en grados Celsius
celsius = float(input("ingrese la temperatura en grados Celsius: "))

#Convertir a Fahrenheit
fahrenheit = (celsius * 9/5) + 32

#Convertir a Kelvin
kelvin = celsius + 273.15

#Mostrar resultados
print("Temperatura en Fahrenheit:", fahrenheit)
print("Temperatura en Kelvin:", kelvin)




#Desafio 8: Verificar múltiplos de varios números

#Pedir numero entero
numero = int(input("ingrese numero entero: "))

#Verifica multiples de 2
if numero % 2 == 0:
    print("es multiple de 2")
else:
    print("no es multiple de 2")

#Verifica multiples de 3
if numero % 3 == 0:
    print(" es multiple de 3")
else:
    print("no es multiple de 3")

#Verifica multiples de 5
if numero % 5 == 0:
    print("es mutiple de 5")
else:
    print("no multiple de 5")

#Verifica multiples de 7
if numero % 7 == 0:
    print("es multiple de 7")
else:
    print("no es multiple de 7")

#Verifica multiples de 9
if numero % 9 == 0:
    print("es multiple de 9")
else:
    print("no es multiple de 9")

#Verifica multiples de 10
if numero % 10 == 0:
    print("es multiple de 10")
else:
    print("no es multiple de 10")

#Verifica multiples de 11
if numero % 11 == 0:
    print("es multiple de 11")
else:
    print("no es multiple de 11")

