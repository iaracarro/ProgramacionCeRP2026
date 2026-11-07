# Desafio Extra 4

eventos = [
    ("2026-10-25 09:00", "Ana", "inicio_sesion"),
    ("2026-10-25 09:15", "Luis", "compra"),
    ("2026-10-25 09:30", "Ana", "compra"),
    ("2026-10-25 10:00", "Pedro", "inicio_sesion"),
    ("2026-10-25 10:15", "Ana", "cierre_sesion"),
    ("2026-10-25 10:30", "Luis", "compra")
]

# Consultar los eventos de un usuario
usuario_buscado = "Ana"

print(f"Eventos de {usuario_buscado}:")

for timestamp, usuario, accion in eventos:
    if usuario == usuario_buscado:
        print(timestamp, accion)

# Contar cuántas veces ocurrió cada acción
conteo_acciones = {}

for timestamp, usuario, accion in eventos:
    if accion in conteo_acciones:
        conteo_acciones[accion] += 1
    else:
        conteo_acciones[accion] = 1

print("\nCantidad de veces que se realizó cada acción:")

for accion, cantidad in conteo_acciones.items():
    print(f"{accion}: {cantidad}")