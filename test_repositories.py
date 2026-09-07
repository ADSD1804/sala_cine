from db.connection import test_connection
from repositories.usuario_repository import UsuarioRepository
from repositories.pelicula_repository import PeliculaRepository


def probar_usuarios():
    print("\n========== USUARIOS ==========")

    repo = UsuarioRepository()

    print("\n1. Usuarios existentes:")
    print(repo.find_all())

    print("\n2. Creando usuario:")
    usuario = repo.create(
        "TEST123",
        "Usuario de prueba",
        "prueba@test.com"
    )
    print(usuario)

    print("\n3. Buscando por cédula:")
    print(repo.find_by_cedula("TEST123"))

    print("\n4. Actualizando:")
    usuario = repo.update(
        "TEST123",
        {
            "nombre": "Usuario actualizado",
            "correo": "actualizado@test.com"
        }
    )
    print(usuario)

    print("\n5. Eliminando:")
    print(repo.delete("TEST123"))

    print("\n6. Comprobando eliminación:")
    print(repo.find_by_cedula("TEST123"))


def probar_peliculas():
    print("\n========== PELÍCULAS ==========")

    repo = PeliculaRepository()

    print("\n1. Películas existentes:")
    print(repo.find_all())

    print("\n2. Creando película:")
    pelicula = repo.create(
        "Película de prueba",
        "Acción",
        "19:00",
        120,
        50
    )
    print(pelicula)

    pelicula_id = pelicula["id"]

    print("\n3. Buscando película:")
    print(repo.find_by_id(pelicula_id))

    print("\n4. Actualizando:")
    pelicula = repo.update(
        pelicula_id,
        {
            "nombre": "Película actualizada",
            "entradas_disponibles": 40
        }
    )
    print(pelicula)

    print("\n5. Eliminando:")
    print(repo.delete(pelicula_id))

    print("\n6. Comprobando eliminación:")
    print(repo.find_by_id(pelicula_id))


if __name__ == "__main__":

    print("========== CONEXIÓN ==========")

    if test_connection():
        probar_usuarios()
        probar_peliculas()