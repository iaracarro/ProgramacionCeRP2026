# Desafio 99

clima = [
    ("Montevideo", 22, 65),
    ("Salto", 30, 45),
    ("Punta del Este", 19, 80),
    ("Paysandú", 27, 55),
    ("Colonia", 24, 70)
]

ciudad_mas_calida = max(clima, key=lambda registro: registro[1])
ciudad_mas_fria = min(clima, key=lambda registro: registro[1])

print("Ciudad con mayor temperatura:", ciudad_mas_calida[0])
print("Temperatura máxima:", ciudad_mas_calida[1], "°C")

print("Ciudad con menor temperatura:", ciudad_mas_fria[0])
print("Temperatura mínima:", ciudad_mas_fria[1], "°C")

humedades = [registro[2] for registro in clima]
promedio_humedad = sum(humedades) / len(humedades)

print("Promedio de humedad:", promedio_humedad, "%")