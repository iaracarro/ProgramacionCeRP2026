# Desafio 98

cursos_ofrecidos = {"Python", "Matemática", "Bases de Datos"}

estudiantes = {
    "Ana": {"Python", "Matemática", "Bases de Datos"},
    "Luis": {"Python", "Matemática"},
    "Sofía": {"Python"},
    "Pedro": {"Bases de Datos"},
    "Carla": {"Python", "Matemática", "Bases de Datos"}
}

print("Estudiantes que completaron todos los cursos:")

for estudiante, cursos in estudiantes.items():
    if cursos_ofrecidos.issubset(cursos):
        print(estudiante)

curso_especifico = "Python"

print(f"\nEstudiantes que solo completaron {curso_especifico}:")

for estudiante, cursos in estudiantes.items():
    if cursos == {curso_especifico}:
        print(estudiante)