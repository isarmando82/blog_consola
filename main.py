# Pre-entrega 6 - Blog por consola con POO y persistencia JSON
# Curso de Python - Coderhouse
# Autor: Armando Ismael
#
# Archivo principal: solo coordina. La logica vive en el paquete blog/.
# Cada opcion del menu esta encapsulada en su propia funcion.

from blog.modelos import Blog
from blog.datos import cargar_posts, guardar_posts, autor_por_defecto, estados_post
from blog.menu import mostrar_menu, pedir_texto, pedir_datos_post
from blog.operaciones import mostrar_posts
from blog.validaciones import validar_todos


# ===============================================================
# FUNCIONES DE CADA OPCION DEL MENU
# ===============================================================

def opcion_ver_posts(blog):
    """Opcion 1: muestra todos los posts del blog."""

    print("Posts disponibles:")
    mostrar_posts(blog.listar_posts())


def opcion_buscar_por_titulo(blog):
    """Opcion 2: pide un termino y muestra los posts cuyo titulo lo contiene."""

    termino = pedir_texto("Buscar por titulo: ")

    if termino == "":
        print("La busqueda no puede estar vacia")
        return

    resultados = blog.buscar_por_titulo(termino)
    if resultados:
        mostrar_posts(resultados)
    else:
        print("No se encontraron resultados")


def opcion_filtrar_por_tag(blog):
    """Opcion 3: pide un tag y muestra los posts que lo tienen."""

    tag = pedir_texto("Filtrar por tag: ")

    if tag == "":
        print("El tag no puede estar vacio")
        return

    resultados = blog.filtrar_por_tag(tag)
    if resultados:
        mostrar_posts(resultados)
    else:
        print("No se encontraron resultados")


def opcion_crear_post(blog):
    """Opcion 4: pide los datos, crea un objeto Post y lo agrega al blog."""

    datos = pedir_datos_post(estados_post)
    if datos is None:
        return

    nuevo = blog.crear_post(
        datos["titulo"],
        datos["contenido"],
        autor_por_defecto(),
        datos["tags"],
        datos["estado"]
    )
    print(f"Post {nuevo.id} creado. Usa la opcion 6 para guardarlo en JSON.")


def opcion_validar_posts(blog):
    """Opcion 5: valida todos los posts e informa el resultado."""

    validar_todos(blog)


def opcion_guardar(blog):
    """Opcion 6: guarda los posts del blog en posts.json."""

    guardar_posts(blog)


# ===============================================================
# EJECUCION PRINCIPAL
# ===============================================================

if __name__ == "__main__":

    # Se cargan los posts desde posts.json y se crea la instancia de Blog
    blog = Blog(cargar_posts())

    while True:
        opcion = mostrar_menu()

        # Si la opcion no era un numero, se vuelve a mostrar el menu
        if opcion is None:
            continue

        if opcion == 1:
            opcion_ver_posts(blog)
        elif opcion == 2:
            opcion_buscar_por_titulo(blog)
        elif opcion == 3:
            opcion_filtrar_por_tag(blog)
        elif opcion == 4:
            opcion_crear_post(blog)
        elif opcion == 5:
            opcion_validar_posts(blog)
        elif opcion == 6:
            opcion_guardar(blog)
        elif opcion == 7:
            # Si hay posts nuevos sin guardar, se pregunta antes de salir
            if blog.hay_cambios:
                respuesta = pedir_texto("Hay cambios sin guardar. ¿Guardar antes de salir? (s/n): ")
                if respuesta.lower() == "s":
                    guardar_posts(blog)
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo")
