# Desafio 46

class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad


class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre


class Transaccion:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.empleados = []
        self.transacciones = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def registrar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)

    def mostrar(self):
        print("Tienda:", self.nombre)

        print("Productos:")
        for producto in self.productos:
            print(producto.nombre, "-", producto.cantidad)

        print("Empleados:")
        for empleado in self.empleados:
            print(empleado.nombre)

        print("Transacciones:")
        for transaccion in self.transacciones:
            print(transaccion.producto, "-", transaccion.cantidad)


tienda1 = Tienda("Tienda Centro")

producto1 = Producto("Arroz", 20)
producto2 = Producto("Leche", 15)

empleado1 = Empleado("Ana")
empleado2 = Empleado("Luis")

tienda1.agregar_producto(producto1)
tienda1.agregar_producto(producto2)

tienda1.agregar_empleado(empleado1)
tienda1.agregar_empleado(empleado2)

transaccion1 = Transaccion("Arroz", 5)
tienda1.registrar_transaccion(transaccion1)

tienda1.mostrar()