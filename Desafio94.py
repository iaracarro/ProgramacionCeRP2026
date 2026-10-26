# Desafio 94

astronomia = {
    "ana@1001problemas.com",
    "luis@1001problemas.com",
    "sofia@1001problemas.com",
    "pedro@1001problemas.com"
}

matematica = {
    "ana@1001problemas.com",
    "luis@1001problemas.com",
    "carla@1001problemas.com"
}

programacion = {
    "ana@1001problemas.com",
    "sofia@1001problemas.com",
    "carla@1001problemas.com",
    "diego@1001problemas.com"
}

# 1. Usuarios que participaron en los tres concursos
todos_los_concursos = astronomia & matematica & programacion

# 2. Usuarios que participaron solamente en Programación
solo_programacion = programacion - astronomia - matematica

# 3. Todos los usuarios únicos que participaron en al menos un concurso
usuarios_unicos = astronomia | matematica | programacion

print("Participaron en los tres concursos:")
print(todos_los_concursos)

print("\nParticiparon solo en Programación:")
print(solo_programacion)

print("\nTodos los usuarios únicos:")
print(usuarios_unicos)