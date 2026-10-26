# Desafio 101

registros_medicos = [
    ("2026-01-10", "Ana", "Gripe"),
    ("2026-01-15", "Luis", "Migraña"),
    ("2026-02-03", "Ana", "Alergia"),
    ("2026-02-20", "Pedro", "Gripe"),
    ("2026-03-01", "Ana", "Gripe"),
    ("2026-03-05", "Luis", "Bronquitis")
]

paciente_buscado = "Ana"

print(f"Historial médico de {paciente_buscado}:")

for fecha, paciente, diagnostico in registros_medicos:
    if paciente == paciente_buscado:
        print(f"Fecha: {fecha} | Diagnóstico: {diagnostico}")

diagnosticos = set()

for fecha, paciente, diagnostico in registros_medicos:
    diagnosticos.add(diagnostico)

print("\nDiagnósticos distintos registrados:", len(diagnosticos))
print("Diagnósticos:", diagnosticos)
