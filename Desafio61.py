# Desafio 61

class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Cargo:", self.cargo)

class Administrador:
    def administrar(self):
        print("Realiza tareas administrativas.")

class Mantenimiento:
    def realizar_mantenimiento(self):
        print("Realiza tareas de mantenimiento.")

class Gerente(Empleado, Administrador):
    def __init__(self, nombre):
        Empleado.__init__(self, nombre, "Gerente")

class Tecnico(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre, "Técnico")
        self.mantenimiento = Mantenimiento()

class Voluntario(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre, "Voluntario")

gerente1 = Gerente("Carlos")
tecnico1 = Tecnico("Lucía")
voluntario1 = Voluntario("Pedro")

gerente1.mostrar_datos()
gerente1.administrar()

print()

tecnico1.mostrar_datos()
tecnico1.mantenimiento.realizar_mantenimiento()

print()

voluntario1.mostrar_datos()