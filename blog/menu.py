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
    print("4. Validar posts")
    print("5. Salir")

    # try-except: si el usuario escribe texto, int() falla y el
    # programa avisa en lugar de cerrarse
    try:
        opcion = int(input("Elegi una opcion: "))
    except ValueError:
        print("Tenes que ingresar un numero del 1 al 5")
        return None

    return opcion


def pedir_texto(mensaje):
    """Pide un texto al usuario y lo retorna sin espacios en los extremos."""

    return input(mensaje).strip()
