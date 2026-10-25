# Desafio 96

inventario = {}

def agregar_producto():
    codigo = input("Ingrese el código del producto: ")

    if codigo in inventario:
        print("El producto ya existe.")
    else:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio: "))
        stock = int(input("Ingrese la cantidad en stock: "))

        inventario[codigo] = {
            "nombre": nombre,
            "precio": precio,
            "stock": stock
        }

        print("Producto agregado correctamente.")

def actualizar_stock():
    codigo = input("Ingrese el código del producto: ")

    if codigo in inventario:
        nuevo_stock = int(input("Ingrese la nueva cantidad en stock: "))
        inventario[codigo]["stock"] = nuevo_stock
        print("Stock actualizado correctamente.")
    else:
        print("El producto no existe.")

def buscar_producto():
    codigo = input("Ingrese el código del producto: ")

    if codigo in inventario:
        print("\n--- DATOS DEL PRODUCTO ---")
        print("Código:", codigo)
        print("Nombre:", inventario[codigo]["nombre"])
        print("Precio:", inventario[codigo]["precio"])
        print("Stock:", inventario[codigo]["stock"])
    else:
        print("El producto no existe.")

while True:
    print("\n--- INVENTARIO DE LA TIENDA ---")
    print("1. Agregar producto")
    print("2. Actualizar stock")
    print("3. Buscar producto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        actualizar_stock()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")