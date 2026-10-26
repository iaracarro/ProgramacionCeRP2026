# Desafio 87

def buscar_libros_por_autor(nombre_archivo, autor_buscado):
    encontrados = False

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(";")

            if len(datos) == 2:
                titulo = datos[0].strip()
                autor = datos[1].strip()

                if autor.lower() == autor_buscado.strip().lower():
                    if not encontrados:
                        print(f"Libros escritos por {autor_buscado}:")
                    print(titulo)
                    encontrados = True

    if not encontrados:
        print(f"No hay coincidencias para el autor {autor_buscado}.")


autor = input("Ingrese el nombre del autor que desea buscar: ")
buscar_libros_por_autor("libros.txt", autor)