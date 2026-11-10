# Pre-entrega 5 - Blog por consola organizado en modulos y paquetes
# Curso de Python - Coderhouse
# Autor: Armando Ismael
#
# Archivo principal: solo coordina. La logica vive en el paquete blog/.
# Cada opcion del menu esta encapsulada en su propia funcion.

from blog.datos import posts
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_todos


# ===============================================================
# FUNCIONES DE CADA OPCION DEL MENU
# ===============================================================

def opcion_ver_posts():
    """Opcion 1: muestra todos los posts."""

    print("Posts disponibles:")
    listar_posts(posts)


def opcion_buscar_por_titulo():
    """Opcion 2: pide un termino y muestra los posts cuyo titulo lo contiene."""

    termino = pedir_texto("Buscar por titulo: ")

    if termino == "":
        print("La busqueda no puede estar vacia")
        return

    resultados = buscar_por_titulo(posts, termino)
    if resultados:
        listar_posts(resultados)
    else:
        print("No se encontraron resultados")


def opcion_filtrar_por_tag():
    """Opcion 3: pide un tag y muestra los posts que lo tienen."""

    tag = pedir_texto("Filtrar por tag: ")

    if tag == "":
        print("El tag no puede estar vacio")
        return

    resultados = filtrar_por_tag(posts, tag)
    if resultados:
        listar_posts(resultados)
    else:
        print("No se encontraron resultados")


def opcion_validar_posts():
    """Opcion 4: valida todos los posts e informa el resultado."""

    validar_todos(posts)


# ===============================================================
# EJECUCION PRINCIPAL
# ===============================================================

if __name__ == "__main__":

    while True:
        opcion = mostrar_menu()

        # Si la opcion no era un numero, se vuelve a mostrar el menu
        if opcion is None:
            continue

        if opcion == 1:
            opcion_ver_posts()
        elif opcion == 2:
            opcion_buscar_por_titulo()
        elif opcion == 3:
            opcion_filtrar_por_tag()
        elif opcion == 4:
            opcion_validar_posts()
        elif opcion == 5:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo")
