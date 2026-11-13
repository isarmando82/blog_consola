# Modelos del blog: clases Autor, Post y Blog
# Curso de Python - Coderhouse
# Autor: Armando Ismael
#
# Este archivo no importa nada de los otros modulos del paquete,
# asi no hay riesgo de imports circulares.


class Autor:
    """Representa a una persona autora del blog."""

    def __init__(self, nombre, bio="", especialidad="", redes_sociales=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        # Si no se pasan redes, se usa una lista vacia nueva
        self.redes_sociales = redes_sociales if redes_sociales is not None else []

    def a_diccionario(self):
        """Convierte el autor en un diccionario compatible con JSON."""

        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Crea un Autor a partir de un diccionario.
        Lanza ValueError si el diccionario no sirve para armar el autor."""

        if not isinstance(datos, dict):
            raise ValueError("el autor no es un diccionario")
        if "nombre" not in datos:
            raise ValueError('al autor le falta la clave "nombre"')

        return cls(
            datos["nombre"],
            datos.get("bio", ""),
            datos.get("especialidad", ""),
            datos.get("redes_sociales", [])
        )

    def __str__(self):
        return self.nombre


class Post:
    """Representa una publicacion del blog.
    El atributo autor es una instancia de la clase Autor (composicion)."""

    CLAVES_OBLIGATORIAS = ("id", "titulo", "contenido", "autor", "tags", "estado")

    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def a_diccionario(self):
        """Convierte el post en un diccionario compatible con JSON.
        El autor tambien se convierte a diccionario."""

        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.a_diccionario(),
            "tags": self.tags,
            "estado": self.estado
        }

    @classmethod
    def desde_diccionario(cls, datos):
        """Crea un Post a partir de un diccionario cargado desde JSON.
        Lanza ValueError si el diccionario esta incompleto."""

        if not isinstance(datos, dict):
            raise ValueError("el post no es un diccionario")

        for clave in cls.CLAVES_OBLIGATORIAS:
            if clave not in datos:
                raise ValueError('falta la clave "' + clave + '"')

        # El autor se reconstruye como objeto Autor, no queda como diccionario
        autor = Autor.desde_diccionario(datos["autor"])

        return cls(
            datos["id"],
            datos["titulo"],
            datos["contenido"],
            autor,
            datos["tags"],
            datos["estado"]
        )

    def tiene_tag(self, tag):
        """Retorna True si el post tiene ese tag, sin distinguir mayusculas."""

        if not isinstance(self.tags, list):
            return False

        for etiqueta in self.tags:
            if isinstance(etiqueta, str) and etiqueta.lower() == tag.lower():
                return True
        return False

    def __str__(self):
        return f"{self.titulo} | Autor: {self.autor} | Estado: {self.estado}"


class Blog:
    """Representa el blog completo y centraliza la logica principal.
    Guarda una lista de objetos Post."""

    def __init__(self, posts=None):
        self.posts = posts if posts is not None else []
        # Indica si hay posts nuevos que todavia no se guardaron en JSON
        self.hay_cambios = False

    def obtener_posts(self):
        """Retorna todos los posts cargados."""

        return self.posts

    def listar_posts(self):
        """Retorna la lista de posts para mostrarlos."""

        return self.posts

    def buscar_por_titulo(self, termino):
        """Retorna los posts cuyo titulo contiene el termino,
        sin distinguir mayusculas de minusculas."""

        termino = termino.lower()
        resultados = []

        for post in self.posts:
            if isinstance(post.titulo, str) and termino in post.titulo.lower():
                resultados.append(post)

        return resultados

    def filtrar_por_tag(self, tag):
        """Retorna los posts que tienen ese tag,
        sin distinguir mayusculas de minusculas."""

        resultados = []

        for post in self.posts:
            if post.tiene_tag(tag):
                resultados.append(post)

        return resultados

    def siguiente_id(self):
        """Calcula el id para un post nuevo: el mayor id actual + 1."""

        ids = [post.id for post in self.posts if isinstance(post.id, int)]
        if ids:
            return max(ids) + 1
        return 1

    def crear_post(self, titulo, contenido, autor, tags, estado):
        """Crea una instancia de Post, la agrega al blog y la retorna."""

        nuevo = Post(self.siguiente_id(), titulo, contenido, autor, tags, estado)
        self.posts.append(nuevo)
        self.hay_cambios = True
        return nuevo

    def a_lista_de_diccionarios(self):
        """Convierte todos los posts en una lista de diccionarios para JSON."""

        return [post.a_diccionario() for post in self.posts]
