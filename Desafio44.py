# Desafio 44: Bibloteca
# Lista donde están todos los libros
biblioteca = []

# Agregar un libro
def agregar_libro(titulo):
    biblioteca.append(titulo)
    print(f'Se agregó "{titulo}" a la biblioteca.')

# Eliminar un libro
def eliminar_libro(titulo):
    if titulo in biblioteca:
        biblioteca.remove(titulo)
        print(f'Se eliminó "{titulo}" de la biblioteca.')
    else:
        print(f'El libro "{titulo}" no está en la biblioteca.')

# Buscar un libro por título
def buscar_libro(titulo):
    if titulo in biblioteca:
        print(f'El libro "{titulo}" está en la biblioteca.')
    else:
        print(f'El libro "{titulo}" no está en la biblioteca.')

# Mostrar todos los libros
def mostrar_libros():
    print("\nLibros disponibles:")

    if len(biblioteca) == 0:
        print("No hay libros en la biblioteca.")
    else:
        for libro in biblioteca:
            print("-", libro)

# Agregamos los cuatro libros a la lista
agregar_libro("El Principito")
agregar_libro("Los Bridgerton")
agregar_libro("Planetas a la vista")
agregar_libro("Martin Fiero")

# Mostramos todos los libros
mostrar_libros()

# Buscamos un libro por su título
buscar_libro("El Principito")

# Eliminamos un libro
eliminar_libro("Los Bridgerton")

# Volvemos a mostrar los libros
mostrar_libros()