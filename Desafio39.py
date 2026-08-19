import datetime

fecha1 = input("Ingrse la premer fecha (DD/MM/AAAA): ")
fecha2 = input("Ingrese la segunda fecha (DD/MM/AAAA): ")

fecha1 = datetime.datetime.strptime(fecha1, "%d/%m/%Y")
fecha2 = datetime.datetime.strptime(fecha2, "%d/%m/%Y")

diferencia = fecha2 - fecha1

print("La diferencia es de", diferencia.days, "dias")