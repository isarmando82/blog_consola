# Datos base del blog
# Curso de Python - Coderhouse
# Autor: Armando Ismael


# --- Perfil del autor ---
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

# --- Lista de posts. Cada uno usa perfil_autor en la clave "autor" ---
# El post con id 4 esta incompleto a proposito, para probar las validaciones.
posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "Como instalar Python, usar la terminal y ejecutar tu primer script.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Que es Django",
        "contenido": "Django es un framework web creado con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con listas",
        "contenido": "Las listas permiten guardar varios elementos en una sola variable.",
        "autor": perfil_autor,
        "tags": ["Python", "Listas"],
        "estado": "archivado"
    },
    {
        # Post incompleto: le falta la clave "contenido"
        "id": 4,
        "titulo": "Post de prueba incompleto",
        "autor": perfil_autor,
        "tags": ["Python"],
        "estado": "borrador"
    }
]
