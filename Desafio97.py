# Desafio 97

facebook = {"Ana", "Luis", "Sofía", "Pedro"}
instagram = {"Ana", "Sofía", "Carla", "Diego"}
twitter = {"Ana", "Luis", "Carla", "Marta"}

# 1. Usuarios que utilizan las tres plataformas
tres_plataformas = facebook & instagram & twitter

# 2. Usuarios que utilizan solamente una plataforma
solo_facebook = facebook - instagram - twitter
solo_instagram = instagram - facebook - twitter
solo_twitter = twitter - facebook - instagram

solo_una = solo_facebook | solo_instagram | solo_twitter

# 3. Usuarios que utilizan al menos dos plataformas
dos_o_mas = (
    (facebook & instagram)
    | (facebook & twitter)
    | (instagram & twitter)
)

print("Usan las tres plataformas:", tres_plataformas)
print("Usan solamente una plataforma:", solo_una)
print("Usan al menos dos plataformas:", dos_o_mas)