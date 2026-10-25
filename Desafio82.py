# Desafio 82


def buscar_calificacion(matriz, estudiantes, materias, calificacion_buscada):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == calificacion_buscada:
                return estudiantes[i], materias[j]

    return None


estudiantes = ["Ana", "Luis", "Sofía"]
materias = ["Matemática", "Informática", "Inglés"]

calificaciones = [
    [8, 10, 7],
    [6, 9, 8],
    [10, 7, 9]
]

resultado = buscar_calificacion(
    calificaciones, estudiantes, materias, 9
)

if resultado:
    estudiante, materia = resultado
    print(f"Calificación encontrada: {estudiante}, materia: {materia}")
else:
    print("Calificación no encontrada")
