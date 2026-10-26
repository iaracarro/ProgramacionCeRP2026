# Desafio 100

torneo_a = {"Ana", "Luis", "Pedro", "Sofía"}
torneo_b = {"Ana", "Luis", "Carla", "Diego"}
torneo_c = {"Ana", "Pedro", "Carla", "Marta"}

todos_los_torneos = torneo_a & torneo_b & torneo_c

solo_a = torneo_a - torneo_b - torneo_c
solo_b = torneo_b - torneo_a - torneo_c
solo_c = torneo_c - torneo_a - torneo_b

solo_un_torneo = solo_a | solo_b | solo_c

atletas_unicos = torneo_a | torneo_b | torneo_c

print("Atletas en todos los torneos:", todos_los_torneos)
print("Atletas en un solo torneo:", solo_un_torneo)
print("Total de atletas únicos:", len(atletas_unicos))
