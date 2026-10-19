import pytest
from unittest.mock import Mock

from services.compra_service import CompraService


@pytest.fixture
def repositorios():
    compra_repo = Mock()
    usuario_repo = Mock()
    pelicula_repo = Mock()

    usuario_repo.find_by_cedula.return_value = {
        "id": 1,
        "cedula": "1004345432",
        "nombre": "Usuario Prueba",
        "correo": "prueba@test.com",
    }

    pelicula_repo.find_by_code.return_value = {
        "id": 1,
        "codigo": "105",
        "nombre": "La Prueba 2",
        "genero": "Suspenso",
        "hora_funcion": "16:20",
        "duracion": 190,
        "entradas_disponibles": 10,
    }

    compra_repo.create.return_value = {
        "id": 1,
        "usuario_cedula": "1004345432",
        "pelicula_codigo": "105",
        "cantidad": 3,
        "total": 36000,
    }

    servicio = CompraService(
        compra_repository=compra_repo,
        usuario_repository=usuario_repo,
        pelicula_repository=pelicula_repo,
    )

    return servicio, compra_repo, usuario_repo, pelicula_repo


def test_listar_compras(repositorios):
    servicio, compra_repo, _, _ = repositorios
    compras = [{"id": 1}, {"id": 2}]
    compra_repo.find_all.return_value = compras

    assert servicio.listar_compras() == compras
    compra_repo.find_all.assert_called_once_with()


def test_buscar_por_id(repositorios):
    servicio, compra_repo, _, _ = repositorios
    compra_repo.find_by_id.return_value = {"id": 1}

    assert servicio.buscar_por_id(1) == {"id": 1}
    compra_repo.find_by_id.assert_called_once_with(1)


@pytest.mark.parametrize("compra_id", [0, -1, "1", None, True])
def test_buscar_por_id_invalido(repositorios, compra_id):
    servicio, compra_repo, _, _ = repositorios

    with pytest.raises(ValueError):
        servicio.buscar_por_id(compra_id)

    compra_repo.find_by_id.assert_not_called()


def test_buscar_por_usuario(repositorios):
    servicio, compra_repo, _, _ = repositorios
    compra = {"usuario_cedula": "1004345432"}
    compra_repo.find_by_usuario.return_value = compra

    assert servicio.buscar_por_usuario(" 1004345432 ") == compra
    compra_repo.find_by_usuario.assert_called_once_with("1004345432")


def test_buscar_por_usuario_sin_cedula(repositorios):
    servicio, compra_repo, _, _ = repositorios

    with pytest.raises(ValueError):
        servicio.buscar_por_usuario(" ")

    compra_repo.find_by_usuario.assert_not_called()


def test_buscar_por_pelicula(repositorios):
    servicio, compra_repo, _, _ = repositorios
    compra = {"pelicula_codigo": "105"}
    compra_repo.find_by_pelicula.return_value = compra

    assert servicio.buscar_por_pelicula(" 105 ") == compra
    compra_repo.find_by_pelicula.assert_called_once_with("105")


def test_buscar_por_pelicula_sin_codigo(repositorios):
    servicio, compra_repo, _, _ = repositorios

    with pytest.raises(ValueError):
        servicio.buscar_por_pelicula(" ")

    compra_repo.find_by_pelicula.assert_not_called()


def test_crear_compra(repositorios):
    servicio, compra_repo, usuario_repo, pelicula_repo = repositorios

    compra = servicio.crear_compra("1004345432", "105", 3, 36000)

    assert compra["usuario_cedula"] == "1004345432"
    assert compra["pelicula_codigo"] == "105"
    assert compra["cantidad"] == 3
    assert compra["total"] == 36000

    usuario_repo.find_by_cedula.assert_called_once_with("1004345432")
    pelicula_repo.find_by_code.assert_called_once_with("105")
    compra_repo.create.assert_called_once_with("1004345432", "105", 3, 36000)


def test_crear_compra_usuario_inexistente(repositorios):
    servicio, compra_repo, usuario_repo, _ = repositorios
    usuario_repo.find_by_cedula.return_value = None

    with pytest.raises(ValueError, match="No existe un usuario"):
        servicio.crear_compra("1004345432", "105", 3, 36000)

    compra_repo.create.assert_not_called()


def test_crear_compra_pelicula_inexistente(repositorios):
    servicio, compra_repo, _, pelicula_repo = repositorios
    pelicula_repo.find_by_code.return_value = None

    with pytest.raises(ValueError, match="No existe una película"):
        servicio.crear_compra("1004345432", "105", 3, 36000)

    compra_repo.create.assert_not_called()


@pytest.mark.parametrize(
    "cantidad",
    [0, -1, 1.5, "3", None, True],
)
def test_crear_compra_cantidad_invalida(repositorios, cantidad):
    servicio, compra_repo, _, _ = repositorios

    with pytest.raises(ValueError, match="cantidad"):
        servicio.crear_compra("1004345432", "105", cantidad, 36000)

    compra_repo.create.assert_not_called()


@pytest.mark.parametrize(
    "total",
    [-1, "36000", None, True, float("nan"), float("inf")],
)
def test_crear_compra_total_invalido(repositorios, total):
    servicio, compra_repo, _, _ = repositorios

    with pytest.raises(ValueError, match="total"):
        servicio.crear_compra("1004345432", "105", 3, total)

    compra_repo.create.assert_not_called()


@pytest.mark.parametrize(
    "cedula,codigo",
    [
        ("", "105"),
        ("1004345432", ""),
        (None, "105"),
        ("1004345432", None),
    ],
)
def test_crear_compra_datos_obligatorios(repositorios, cedula, codigo):
    servicio, compra_repo, _, _ = repositorios

    with pytest.raises(ValueError):
        servicio.crear_compra(cedula, codigo, 3, 36000)

    compra_repo.create.assert_not_called()


def test_eliminar_compra(repositorios):
    servicio, compra_repo, _, _ = repositorios
    compra_repo.delete.return_value = True

    assert servicio.eliminar_compra(1) is True
    compra_repo.delete.assert_called_once_with(1)


def test_eliminar_compra_inexistente(repositorios):
    servicio, compra_repo, _, _ = repositorios
    compra_repo.delete.return_value = False

    assert servicio.eliminar_compra(99) is False
    compra_repo.delete.assert_called_once_with(99)


def test_eliminar_compra_id_invalido(repositorios):
    servicio, compra_repo, _, _ = repositorios

    with pytest.raises(ValueError):
        servicio.eliminar_compra(0)

    compra_repo.delete.assert_not_called()
