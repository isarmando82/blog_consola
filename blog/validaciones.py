# Reglas de validacion de los posts
# Curso de Python - Coderhouse
# Autor: Armando Ismael

# Se importan los estados validos desde datos.py.
# datos.py no importa nada de este archivo, asi que no hay import circular.
from blog.datos import estados_post


def validar_post(post):
    """Recibe un post y revisa que cumpla las reglas esperadas.
    Retorna dos valores: True o False, y un mensaje que explica el resultado."""

    if not isinstance(post, dict):
        return False, "no es un diccionario"

    # Se verifica que existan todas las claves obligatorias
    claves_obligatorias = ("id", "titulo", "contenido", "autor", "tags", "estado")
    for clave in claves_obligatorias:
        if clave not in post:
            return False, 'falta la clave "' + clave + '"'

    titulo = post.get("titulo")
    if not isinstance(titulo, str) or titulo.strip() == "":
        return False, "el titulo esta vacio"

    contenido = post.get("contenido")
    if not isinstance(contenido, str) or contenido.strip() == "":
        return False, "el contenido esta vacio"

    autor = post.get("autor")
    if not isinstance(autor, dict):
        return False, "el autor no es un diccionario"

    if "nombre" not in autor:
        return False, 'el autor no tiene la clave "nombre"'

    if not isinstance(post.get("tags"), list):
        return False, "tags no es una lista"

    if post.get("estado") not in estados_post:
        return False, 'el estado "' + str(post.get("estado")) + '" no es valido'

    return True, "valido"


def validar_todos(lista):
    """Recorre la lista de posts y muestra cuales son validos y cuales tienen errores."""

    for post in lista:
        # El id puede faltar, por eso se usa .get() con un valor por defecto
        if isinstance(post, dict):
            numero = post.get("id", "?")
        else:
            numero = "?"

        valido, mensaje = validar_post(post)

        if valido:
            print(f"Post {numero}: valido")
        else:
            print(f"Post {numero}: error - {mensaje}")
