# Datos base y persistencia JSON del blog
# Curso de Python - Coderhouse
# Autor: Armando Ismael
#
# Este modulo se encarga de cargar los posts desde posts.json
# y de guardarlos. Solo importa desde modelos.py.

import json
from pathlib import Path

from blog.modelos import Autor, Post


# --- Ruta del archivo JSON: queda en la carpeta raiz del proyecto ---
RUTA_POSTS = Path(__file__).resolve().parent.parent / "posts.json"

# --- Perfil del autor por defecto (se usa al crear posts nuevos) ---
perfil_autor = {
    "nombre": "Armando Ismael",
    "bio": "Desarrollador en formacion, escribo sobre Python y automatizacion.",
    "especialidad": "Python y automatizacion de procesos",
    "redes_sociales": ["@isarmando_dev", "@isarmando_py"]
}

# --- Estados posibles de un post (tupla: valores fijos) ---
estados_post = ("borrador", "publicado", "archivado")

# --- Etiquetas del blog (set: no admite duplicados) ---
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python"}


def autor_por_defecto():
    """Retorna un objeto Autor armado con el perfil por defecto."""

    return Autor.desde_diccionario(perfil_autor)


def cargar_posts(ruta=RUTA_POSTS):
    """Lee posts.json y retorna una lista de objetos Post.
    Si el archivo no existe, esta vacio o es invalido, avisa y
    retorna una lista vacia en lugar de cerrar el programa."""

    ruta = Path(ruta)

    if not ruta.exists():
        print(f"Aviso: no se encontro {ruta.name}. Se empieza con el blog vacio.")
        return []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except OSError as error:
        print(f"Error: no se pudo leer {ruta.name} ({error}).")
        return []

    if contenido.strip() == "":
        print(f"Aviso: {ruta.name} esta vacio. Se empieza con el blog vacio.")
        return []

    try:
        datos = json.loads(contenido)
    except json.JSONDecodeError:
        print(f"Error: {ruta.name} tiene contenido invalido (no es JSON). Se empieza con el blog vacio.")
        return []

    if not isinstance(datos, list):
        print(f"Error: {ruta.name} deberia tener una lista de posts. Se empieza con el blog vacio.")
        return []

    # Cada diccionario se convierte de nuevo en un objeto Post
    posts = []
    for posicion, item in enumerate(datos, start=1):
        try:
            posts.append(Post.desde_diccionario(item))
        except ValueError as error:
            print(f"Aviso: el registro {posicion} de {ruta.name} se omitio: {error}.")

    print(f"Se cargaron {len(posts)} posts desde {ruta.name}.")
    return posts


def guardar_posts(blog, ruta=RUTA_POSTS):
    """Convierte los posts del blog a diccionarios y los guarda en posts.json.
    Retorna True si se guardo bien y False si hubo un error."""

    ruta = Path(ruta)

    try:
        datos = blog.a_lista_de_diccionarios()
        # Se arma el texto antes de abrir el archivo: si algo no es
        # compatible con JSON, falla aca y el archivo anterior no se pisa
        texto = json.dumps(datos, ensure_ascii=False, indent=4)
    except (TypeError, AttributeError) as error:
        print("Error: hay datos que no se pueden guardar en JSON. "
              "Los objetos deben convertirse a diccionario antes de guardarse "
              f"({error}).")
        return False

    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
    except OSError as error:
        print(f"Error: no se pudo escribir {ruta.name} ({error}).")
        return False

    blog.hay_cambios = False
    print(f"Se guardaron {len(datos)} posts en {ruta.name}.")
    return True
