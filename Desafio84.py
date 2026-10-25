# Desafio 84

def ordenar_por_promedio(estudiantes):
    for i in range(len(estudiantes)):
        mayor = i

        for j in range(i + 1, len(estudiantes)):
            if estudiantes[j][1] > estudiantes[mayor][1]:
                mayor = j

        estudiantes[i], estudiantes[mayor] = estudiantes[mayor], estudiantes[i]

    return estudiantes


estudiantes = [
    ["Ana", 8.5],
    ["Luis", 6.5],
    ["Sofía", 9.2],
    ["Bruno", 7.8]
]

ordenados = ordenar_por_promedio(estudiantes)

for estudiante in ordenados:
    print(estudiante[0], "-", estudiante[1])