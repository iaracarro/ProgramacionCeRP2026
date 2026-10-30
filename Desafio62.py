# Desafio 62

class Musico:
    def instrumento(self):
        print("El músico toca un instrumento.")


class Guitarrista(Musico):
    def instrumento(self):
        print("El guitarrista toca la guitarra.")


class Baterista(Musico):
    def instrumento(self):
        print("El baterista toca la batería.")

musico1 = Guitarrista()
musico2 = Baterista()

musicos = [musico1, musico2]

for musico in musicos:
    musico.instrumento()