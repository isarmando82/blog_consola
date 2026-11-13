# Reglas de validacion de los posts
# Curso de Python - Coderhouse
# Autor: Armando Ismael
#
# Importa las clases desde modelos.py y los estados desde datos.py.
# Ninguno de esos dos importa este archivo: no hay imports circulares.

from blog.modelos import Autor, Post
from blog.datos import estados_post


def validar_post(post):
    """Recibe un objeto Post y revisa que cumpla las reglas esperadas.
    Retorna dos valores: True o False, y un mensaje que explica el resultado."""

    if not isinstance(post, Post):
        return False, "no es un objeto Post"

    if not isinstance(post.titulo, str) or post.titulo.strip() == "":
        return False, "el titulo esta vacio"

    if not isinstance(post.contenido, str) or post.contenido.strip() == "":
        return False, "el contenido esta vacio"

    if not isinstance(post.autor, Autor):
        return False, "el autor no es un objeto Autor"

    if not isinstance(post.autor.nombre, str) or post.autor.nombre.strip() == "":
        return False, "el autor no tiene nombre"

    if not isinstance(post.tags, list):
        return False, "tags no es una lista"

    if post.estado not in estados_post:
        return False, 'el estado "' + str(post.estado) + '" no es valido'

    return True, "valido"


def validar_todos(blog):
    """Recorre los posts del blog y muestra cuales son validos y cuales tienen errores."""

    posts = blog.obtener_posts()

    if not posts:
        print("No hay posts para validar")
        return

    for post in posts:
        numero = getattr(post, "id", "?")
        valido, mensaje = validar_post(post)

        if valido:
            print(f"Post {numero}: valido")
        else:
            print(f"Post {numero}: error - {mensaje}")
