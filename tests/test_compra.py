from repositories.compra_repository import CompraRepository
from repositories.usuario_repository import UsuarioRepository
from repositories.pelicula_repository import PeliculaRepository

repoUser = UsuarioRepository()
repoMovie = PeliculaRepository()
repoBuy = CompraRepository()

cedula = "1004345432"
codigoPeli = "105"


def test_crear_compra():

    usuario = repoUser.create(cedula, "UsuarioPrueba", "prueba@test.com")

    pelicula = repoMovie.create(codigoPeli, "La Prueba 2", "Suspenso", "16:20", 190, 10)

    compra = repoBuy.create(usuario["cedula"], pelicula["codigo"], 3, 36000)

    assert compra is not None
    assert compra["usuario_cedula"] == cedula
    assert compra["pelicula_codigo"] == codigoPeli
    assert compra["cantidad"] == 3
    assert compra["total"] == 36000
    repoBuy.delete(compra["id"])
    repoUser.delete(cedula)
    repoMovie.delete(codigoPeli)


def test_buscar_id():

    usuario = repoUser.create(cedula, "Usuario de Prueba ID", "prueba@testID.net")

    pelicula = repoMovie.create(
        codigoPeli, "La Prueba 2 ID", "Suspenso", "16:20", 190, 0
    )

    compra = repoBuy.create(usuario["cedula"], pelicula["codigo"], 3, 36000)

    idBuscar = compra["id"]

    resultado = repoBuy.find_by_id(idBuscar)

    assert resultado is not None
    assert resultado["id"] == idBuscar
    assert resultado["pelicula_codigo"] == codigoPeli
    assert resultado["usuario_cedula"] == cedula

    repoBuy.delete(idBuscar)
    repoUser.delete(cedula)
    repoMovie.delete(codigoPeli)


def test_buscar_usuario():

    usuario = repoUser.create(cedula, "Usuario de Prueba", "prueba@test.net")

    pelicula = repoMovie.create(codigoPeli, "La Prueba 2", "Suspenso", "16:20", 190, 0)

    compra = repoBuy.create(usuario["cedula"], pelicula["codigo"], 3, 36000)

    id = compra["id"]

    resultado = repoBuy.find_by_usuario(cedula)

    assert resultado is not None
    assert resultado["usuario_cedula"] == cedula
    assert resultado["pelicula_codigo"] == codigoPeli
    assert resultado["cantidad"] == 3
    assert resultado["total"] == 36000

    repoBuy.delete(id)
    repoUser.delete(cedula)
    repoMovie.delete(codigoPeli)


def test_buscar_pelicula():

    usuario = repoUser.create(cedula, "Usuario de Prueba", "prueba@test.net")

    pelicula = repoMovie.create(codigoPeli, "La Prueba 2", "Suspenso", "16:20", 190, 0)

    compra = repoBuy.create(usuario["cedula"], pelicula["codigo"], 3, 36000)

    id = compra["id"]

    resultado = repoBuy.find_by_pelicula(codigoPeli)

    assert resultado is not None
    assert resultado["pelicula_codigo"] == codigoPeli
    assert resultado["usuario_cedula"] == cedula
    assert resultado["cantidad"] == 3
    assert resultado["total"] == 36000

    repoBuy.delete(id)
    repoUser.delete(cedula)
    repoMovie.delete(codigoPeli)


def test_borrar_compra():

    usuario = repoUser.create(cedula, "Usuario de Prueba", "prueba@test.net")

    pelicula = repoMovie.create(codigoPeli, "La Prueba 2", "Suspenso", "16:20", 190, 0)

    compra = repoBuy.create(usuario["cedula"], pelicula["codigo"], 3, 36000)

    id_compra = compra["id"]

    resultado = repoBuy.delete(id_compra)

    assert resultado is True
    assert repoBuy.find_by_id(id_compra) is None

    repoUser.delete(cedula)
    repoMovie.delete(codigoPeli)
