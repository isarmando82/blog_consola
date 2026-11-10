# Blog por consola organizado en módulos y paquetes

Pre-entrega 5 — Curso de Python, Coderhouse
Autor: Armando Ismael

## Qué hace

Sistema de blog por consola que permite listar, buscar, filtrar y validar publicaciones.

Es el mismo sistema del Módulo 4, reorganizado en varios archivos: los datos, el menú, las operaciones y las validaciones viven cada uno en su propio módulo, dentro del paquete `blog/`.

## Cómo ejecutarlo

Requisitos: Python 3.6 o superior. No usa librerías externas.

El archivo que se ejecuta es `main.py`, siempre desde la carpeta raíz del proyecto:

```
cd blog_consola
python main.py
```

En Windows, desde PowerShell:

```
cd C:\coderhouse\blog_consola
python main.py
```

Si se ejecuta desde otra carpeta, Python no encuentra el paquete `blog` y aparece un error de importación.

## Organización de la carpeta

```
blog_consola/
│
├── main.py
├── README.md
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

## Responsabilidad de cada archivo

| Archivo | Qué hace |
|---|---|
| `main.py` | Archivo principal. Importa las piezas del paquete. Cada opción del menú está encapsulada en su propia función (`opcion_ver_posts()`, `opcion_buscar_por_titulo()`, `opcion_filtrar_por_tag()`, `opcion_validar_posts()`), y el bloque `if __name__ == "__main__":` solo muestra el menú y llama a la función que corresponde. |
| `blog/__init__.py` | Hace que Python reconozca la carpeta `blog/` como paquete. |
| `blog/datos.py` | Estructuras base: `perfil_autor`, `estados_post`, `etiquetas_blog` y `posts`. El autor es un diccionario anidado dentro de cada post. |
| `blog/menu.py` | `mostrar_menu()` muestra las opciones y captura la elegida; `pedir_texto()` pide los términos de búsqueda. Todo el `input()` está acá. |
| `blog/operaciones.py` | `listar_posts()`, `buscar_por_titulo()` y `filtrar_por_tag()`. Reciben la lista de posts por parámetro. |
| `blog/validaciones.py` | `validar_post()` revisa las reglas de cada post; `validar_todos()` informa el resultado de todos. |

## Funcionalidades del menú

```
--- MENU DEL BLOG ---
1. Ver todos los posts
2. Buscar por titulo
3. Filtrar por tag
4. Validar posts
5. Salir
```

1. **Ver todos los posts**: muestra título, autor y estado de cada post.
2. **Buscar por título**: muestra los posts cuyo título contiene el término, sin distinguir mayúsculas y minúsculas.
3. **Filtrar por tag**: muestra los posts que tienen esa etiqueta, sin distinguir mayúsculas y minúsculas.
4. **Validar posts**: revisa cada post e informa si es válido o qué error tiene.
5. **Salir**: muestra un mensaje de despedida y cierra el programa.

El post 4 está incompleto a propósito (le falta el contenido) para comprobar que la validación funciona.

## Imports y dependencias

```python
from blog.datos import posts
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_todos
```

`validaciones.py` importa `estados_post` desde `datos.py`. `datos.py` no importa nada, así que no hay imports circulares.
