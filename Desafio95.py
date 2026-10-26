# Desafio 95

ventas = [
    ("P01", 3, 100),
    ("P02", 5, 50),
    ("P01", 2, 100),
    ("P03", 4, 80),
    ("P02", 1, 50),
    ("P03", 2, 80)
]

ingreso_total = 0
cantidades_por_producto = {}

for id_producto, cantidad, precio_unitario in ventas:
    ingreso_total += cantidad * precio_unitario

    if id_producto in cantidades_por_producto:
        cantidades_por_producto[id_producto] += cantidad
    else:
        cantidades_por_producto[id_producto] = cantidad

print(f"Ingreso total: ${ingreso_total}")

producto_mas_vendido = max(
    cantidades_por_producto,
    key=cantidades_por_producto.get
)

print("Producto más vendido:", producto_mas_vendido)
print("Unidades vendidas:", cantidades_por_producto[producto_mas_vendido])