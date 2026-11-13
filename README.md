# Blog por consola con POO y persistencia JSON

Pre-entrega 6 — Curso de Python, Coderhouse

Autor: Armando Ismael

## Qué hace

Sistema de blog por consola que permite listar, buscar, filtrar, crear y validar publicaciones, y guardarlas en un archivo `posts.json` para que se conserven entre ejecuciones.

Es el mismo proyecto modular del Módulo 5, refactorizado a Programación Orientada a Objetos: los autores, los posts y el blog ahora son clases, y los datos se cargan y se guardan en JSON.

## Cómo ejecutarlo

Requisitos: Python 3.6 o superior. No usa librerías externas (solo `json` y `pathlib`, que vienen con Python).

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

Al iniciar, el programa carga los posts desde `posts.json`.

## Organización de la carpeta

```
blog_consola/
│
├── main.py
├── README.md
├── posts.json
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── modelos.py
    ├── operaciones.py
    └── validaciones.py
```

## Clases principales (`blog/modelos.py`)

| Clase | Responsabilidad |
|---|---|
| `Autor` | Representa a la persona autora: `nombre`, `bio`, `especialidad` y `redes_sociales`. |
| `Post` | Representa una publicación: `id`, `titulo`, `contenido`, `autor`, `tags` y `estado`. El atributo `autor` es una instancia de `Autor` (composición), no un texto. |
| `Blog` | Centraliza la lógica principal. Tiene el atributo `posts`, una lista de objetos `Post`, y los métodos `listar_posts()`, `buscar_por_titulo()`, `filtrar_por_tag()`, `crear_post()`, `obtener_posts()` y `a_lista_de_diccionarios()`. |

Conversión entre objetos y diccionarios:

- `Autor.a_diccionario()` y `Post.a_diccionario()` convierten cada objeto en un diccionario compatible con JSON. El post también convierte a su autor.
- `Autor.desde_diccionario()` y `Post.desde_diccionario()` hacen el camino inverso: reconstruyen los objetos a partir de los diccionarios leídos del JSON. Si al diccionario le falta una clave, lanzan un `ValueError` con un mensaje claro.

## Responsabilidad de cada archivo

| Archivo | Qué hace |
|---|---|
| `main.py` | Punto de entrada. Carga los posts, crea la instancia de `Blog`, muestra el menú y llama al método correspondiente. Cada opción del menú está en su propia función, y la ejecución está dentro de `if __name__ == "__main__":`. |
| `blog/modelos.py` | Clases `Autor`, `Post` y `Blog`. |
| `blog/datos.py` | Persistencia: `cargar_posts()` lee `posts.json` y devuelve objetos `Post`; `guardar_posts()` convierte el blog a diccionarios y lo escribe. También tiene los datos base: el perfil del autor, los estados válidos y las etiquetas. |
| `blog/menu.py` | Todo el `input()`: `mostrar_menu()`, `pedir_texto()` y `pedir_datos_post()`, que pide y controla los datos de un post nuevo. |
| `blog/operaciones.py` | `mostrar_posts()`, que muestra en pantalla título, autor y estado de una lista de posts. |
| `blog/validaciones.py` | `validar_post()` revisa las reglas de cada objeto `Post`; `validar_todos()` informa el resultado de todos los posts del blog. |
| `posts.json` | Archivo donde se guardan los posts. |

## Cómo se guarda y se carga la información

**Al iniciar:** `cargar_posts()` lee `posts.json`, que contiene una lista de diccionarios. Cada diccionario se convierte en un objeto `Post` con `Post.desde_diccionario()`, que también arma su objeto `Autor`. Con esa lista se crea la instancia de `Blog`.

**Al guardar:** `guardar_posts()` le pide al blog `a_lista_de_diccionarios()`, que llama a `a_diccionario()` de cada post, y escribe el resultado en `posts.json` con el módulo `json`.

Se guarda con la opción 6 del menú. Al salir con la opción 7, si se crearon posts que todavía no se guardaron, el programa pregunta si se quieren guardar.

## Funcionalidades del menú

```
--- MENU DEL BLOG ---
1. Ver todos los posts
2. Buscar por titulo
3. Filtrar por tag
4. Crear nuevo post
5. Validar posts
6. Guardar posts en JSON
7. Salir
```

1. **Ver todos los posts**: muestra título, autor y estado de cada post.
2. **Buscar por título**: muestra los posts cuyo título contiene el término, sin distinguir mayúsculas y minúsculas.
3. **Filtrar por tag**: muestra los posts que tienen esa etiqueta, sin distinguir mayúsculas y minúsculas.
4. **Crear nuevo post**: pide título, contenido, tags y estado, crea un objeto `Post` y lo agrega al blog. El autor es el perfil por defecto.
5. **Validar posts**: revisa cada post e informa si es válido o qué error tiene. El post 4 tiene el contenido vacío a propósito para probar la validación.
6. **Guardar posts en JSON**: guarda todos los posts en `posts.json`.
7. **Salir**: si hay cambios sin guardar, pregunta si guardarlos; después muestra un mensaje de despedida y cierra el programa.

## Manejo de errores

El programa no se cierra ante estos casos y muestra un mensaje claro:

- `posts.json` no existe, está vacío o tiene contenido inválido: avisa y empieza con el blog vacío.
- Un registro del JSON está incompleto: se omite ese registro, se informa qué clave falta y se cargan los demás.
- Opción del menú que no es un número o que está fuera de rango.
- Campos vacíos al crear un post, o un estado que no es válido.
- Datos que no son compatibles con JSON al guardar (por ejemplo, un objeto que no se convirtió a diccionario): avisa y no pisa el archivo anterior.

## Qué cambió respecto de la pre-entrega 5

- Se agregó `blog/modelos.py` con las clases `Autor`, `Post` y `Blog`. El sistema ahora trabaja con objetos, no con diccionarios.
- `datos.py` pasó a encargarse de la persistencia: los posts ya no están escritos en el código, se cargan desde `posts.json` y se guardan ahí.
- La búsqueda y el filtrado pasaron de `operaciones.py` a métodos de la clase `Blog`.
- `validaciones.py` ahora valida objetos `Post` y `Autor`.
- El menú tiene dos opciones nuevas: crear un post y guardar en JSON.
- `main.py` crea una instancia de `Blog` y llama a sus métodos.

## Imports y dependencias

```python
from blog.modelos import Blog
from blog.datos import cargar_posts, guardar_posts, autor_por_defecto, estados_post
from blog.menu import mostrar_menu, pedir_texto, pedir_datos_post
from blog.operaciones import mostrar_posts
from blog.validaciones import validar_todos
```

`modelos.py` no importa nada del paquete. `datos.py` importa de `modelos.py`, y `validaciones.py` importa de `modelos.py` y de `datos.py`. Las dependencias van en un solo sentido, así que no hay imports circulares.
