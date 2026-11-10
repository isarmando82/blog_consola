# Operaciones del blog: listar, buscar y filtrar
# Curso de Python - Coderhouse
# Autor: Armando Ismael
#
# Todas las funciones reciben la lista de posts por parametro:
# no dependen de variables globales.


def listar_posts(lista):
    """Recibe una lista de posts y muestra el titulo, el autor y el estado de cada uno."""

    if not lista:
        print("No hay posts para mostrar")
        return

    for post in lista:
        # .get() evita el KeyError si la clave no existe
        titulo = post.get("titulo", "(sin titulo)")
        estado = post.get("estado", "(sin estado)")

        autor = post.get("autor")
        # El autor es un diccionario anidado: se accede en dos pasos
        if isinstance(autor, dict):
            nombre = autor.get("nombre", "(sin nombre)")
        else:
            nombre = "(autor invalido)"

        print("-", titulo, "| Autor:", nombre, "| Estado:", estado)


def buscar_por_titulo(lista, termino):
    """Recibe la lista de posts y un termino.
    Retorna la lista de posts cuyo titulo contiene ese termino,
    sin distinguir mayusculas de minusculas."""

    resultados = []
    termino = termino.lower()

    for post in lista:
        titulo = post.get("titulo", "")
        if isinstance(titulo, str) and termino in titulo.lower():
            resultados.append(post)

    return resultados


def filtrar_por_tag(lista, tag):
    """Recibe la lista de posts y un tag.
    Retorna la lista de posts que tienen ese tag,
    sin distinguir mayusculas de minusculas."""

    resultados = []
    tag = tag.lower()

    for post in lista:
        tags = post.get("tags")

        # Si tags no es una lista, se saltea ese post en lugar de fallar
        if not isinstance(tags, list):
            continue

        for etiqueta in tags:
            if isinstance(etiqueta, str) and etiqueta.lower() == tag:
                resultados.append(post)
                break

    return resultados
