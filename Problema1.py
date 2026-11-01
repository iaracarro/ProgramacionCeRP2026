# Problema 1: Análisis de ventas mensuales

import array

ventas_mensuales = array.array('i', [
    120, 135, 150, 145, 160, 155,
    130, 140, 125, 170, 160, 180
])

# Venta total anual
total_anual = sum(ventas_mensuales)
print("Venta total anual:", total_anual)

# Promedio mensual
promedio_mensual = total_anual / len(ventas_mensuales)
print(f"Promedio mensual: {promedio_mensual:.2f}")

# Mes con venta más baja y más alta
mes_baja = ventas_mensuales.index(min(ventas_mensuales)) + 1
mes_alta = ventas_mensuales.index(max(ventas_mensuales)) + 1

print("Mes con venta más baja:", mes_baja)
print("Mes con venta más alta:", mes_alta)

print("Venta mínima:", min(ventas_mensuales))
print("Venta máxima:", max(ventas_mensuales))