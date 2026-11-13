# Operaciones de presentacion del blog
# Curso de Python - Coderhouse
# Autor: Armando Ismael
#
# La busqueda y el filtrado ahora son metodos de la clase Blog (modelos.py).
# Aca queda la funcion que muestra en pantalla una lista de objetos Post.


def mostrar_posts(lista):
    """Recibe una lista de objetos Post y muestra titulo, autor y estado de cada uno."""

    if not lista:
        print("No hay posts para mostrar")
        return

    for post in lista:
        # str(post) usa el metodo __str__ de la clase Post
        print("-", post)
