# Desafio 83

def buscar_estudiante(estudiantes, nombre_buscado):
    izquierda = 0
    derecha = len(estudiantes) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if estudiantes[medio] == nombre_buscado:
            print(f"Estudiante encontrado: {nombre_buscado}")
            return

        elif estudiantes[medio] < nombre_buscado:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    print("Estudiante no encontrado.")


estudiantes = [
    "Ana",
    "Bruno",
    "Carlos",
    "Lucía",
    "María",
    "Sofía"
]

buscar_estudiante(estudiantes, "Lucía")
buscar_estudiante(estudiantes, "Pedro")