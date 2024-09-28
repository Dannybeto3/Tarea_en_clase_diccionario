# Realizar la captura desde el teclado de los siguientes datos
# Nombre del libro, categoría, año de publicación, número de hojas, autor.
# Guardar en la variable libros

def capturar_datos():
    nombre_libro = input("Nombre del libro: ")
    categoria = input("Categoría: ")
    año_publicacion = input("Año de publicación: ")
    numero_hojas = input("Número de hojas: ")
    autor = input("Autor: ")


    libro = {
        "Nombre del libro": nombre_libro,
        "Categoría": categoria,
        "Año de publicación": año_publicacion,
        "Número de hojas": numero_hojas,
        "Autor": autor
    }

    return libro

def imprimir_listado(libros):
    for i, libro in enumerate(libros, start=1):
        print(f"\nLibro {i}:")
        for clave, valor in libro.items():
            print(f"{clave}: {valor}")

listado_libros = []


while True:
    libro = capturar_datos()
    listado_libros.append(libro)

    continuar = input("¿Deseas ingresar otro libro? (SI/NO): ")
    if continuar.lower() != 's':
        break

# Imprimir el listado de libros
imprimir_listado(listado_libros)