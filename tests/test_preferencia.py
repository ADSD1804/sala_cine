from repositories.preferencia_repository import PreferenciaRepository
from repositories.usuario_repository import UsuarioRepository
from repositories.usuario_preferencia_repository import UsuarioPreferenciaRepository

repoPreferencia = PreferenciaRepository()
repoUsuario = UsuarioRepository()
repoUsuarioPreferencia = UsuarioPreferenciaRepository()


def test_crear_preferencia():
    genero_pelicula = "Terror"
    preferencia = repoPreferencia.create(genero_pelicula)

    assert preferencia is not None
    assert preferencia["genero_pelicula"] == genero_pelicula

    repoPreferencia.delete(preferencia["id"])


def test_buscar_todos():
    genero_pelicula = "Comedia"
    preferencia = repoPreferencia.create(genero_pelicula)

    resultado = repoPreferencia.find_all()

    assert resultado is not None
    assert resultado["genero_pelicula"] == genero_pelicula

    repoPreferencia.delete(preferencia["id"])


def test_buscar_por_id():
    genero_pelicula = "Accion"
    preferencia = repoPreferencia.create(genero_pelicula)

    resultado = repoPreferencia.find_by_id(preferencia["id"])

    assert resultado is not None
    assert resultado["id"] == preferencia["id"]
    assert resultado["genero_pelicula"] == genero_pelicula

    repoPreferencia.delete(preferencia["id"])


def test_actualizar_preferencia():
    genero_pelicula = "Drama"
    preferencia = repoPreferencia.create(genero_pelicula)

    nuevo_genero = "Romance"
    repoPreferencia.update(preferencia["id"], nuevo_genero)

    resultado = repoPreferencia.find_by_id(preferencia["id"])

    assert resultado is not None
    assert resultado["id"] == preferencia["id"]
    assert resultado["genero_pelicula"] == nuevo_genero

    repoPreferencia.delete(preferencia["id"])


def test_eliminar_preferencia():
    genero_pelicula = "Ciencia Ficción"
    preferencia = repoPreferencia.create(genero_pelicula)

    repoPreferencia.delete(preferencia["id"])

    resultado = repoPreferencia.find_by_id(preferencia["id"])

    assert resultado is None
