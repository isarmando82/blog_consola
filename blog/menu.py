# Menu e interaccion con el usuario
# Curso de Python - Coderhouse
# Autor: Armando Ismael


def mostrar_menu():
    """Muestra el menu y retorna la opcion elegida como numero.
    Si el usuario escribe algo que no es un numero, retorna None."""

    print("--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")

    # try-except: si el usuario escribe texto, int() falla y el
    # programa avisa en lugar de cerrarse
    try:
        opcion = int(input("Elegi una opcion: "))
    except ValueError:
        print("Tenes que ingresar un numero del 1 al 7")
        return None

    return opcion


def pedir_texto(mensaje):
    """Pide un texto al usuario y lo retorna sin espacios en los extremos."""

    return input(mensaje).strip()


def pedir_datos_post(estados_validos):
    """Pide los datos de un post nuevo.
    Retorna un diccionario con los datos, o None si alguno no es valido."""

    titulo = pedir_texto("Titulo: ")
    if titulo == "":
        print("Error: el titulo no puede estar vacio. No se creo el post.")
        return None

    contenido = pedir_texto("Contenido: ")
    if contenido == "":
        print("Error: el contenido no puede estar vacio. No se creo el post.")
        return None

    texto_tags = pedir_texto("Tags separados por coma (ej: Python, Web): ")
    tags = [tag.strip() for tag in texto_tags.split(",") if tag.strip() != ""]
    if not tags:
        print("Error: tenes que ingresar al menos un tag. No se creo el post.")
        return None

    estado = pedir_texto("Estado (" + ", ".join(estados_validos) + "): ").lower()
    if estado not in estados_validos:
        print("Error: el estado tiene que ser uno de estos: "
              + ", ".join(estados_validos) + ". No se creo el post.")
        return None

    return {"titulo": titulo, "contenido": contenido, "tags": tags, "estado": estado}
