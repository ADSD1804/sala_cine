import pytest
from unittest.mock import Mock

from services.pelicula_service import PeliculaService


@pytest.fixture
def repo_mock():
    return Mock()


@pytest.fixture
def servicio(repo_mock):
    return PeliculaService(pelicula_repository=repo_mock)


@pytest.fixture
def pelicula():
    return {
        "id": 1,
        "codigo": "CINE001",
        "nombre": "Película de prueba",
        "genero": "Acción",
        "hora_funcion": "19:00",
        "duracion": 120,
        "entradas_disponibles": 50,
    }


def test_listar_peliculas(servicio, repo_mock, pelicula):
    repo_mock.find_all.return_value = [pelicula]

    resultado = servicio.listar_peliculas()

    assert resultado == [pelicula]
    repo_mock.find_all.assert_called_once_with()


def test_buscar_por_codigo(servicio, repo_mock, pelicula):
    repo_mock.find_by_code.return_value = pelicula

    resultado = servicio.buscar_por_codigo(" CINE001 ")

    assert resultado == pelicula
    repo_mock.find_by_code.assert_called_once_with("CINE001")


def test_buscar_por_codigo_vacio(servicio, repo_mock):
    with pytest.raises(ValueError, match="codigo"):
        servicio.buscar_por_codigo(" ")

    repo_mock.find_by_code.assert_not_called()


def test_crear_pelicula(servicio, repo_mock, pelicula):
    repo_mock.find_by_code.return_value = None
    repo_mock.create.return_value = pelicula

    resultado = servicio.crear_pelicula(
        " CINE001 ",
        " Película de prueba ",
        " Acción ",
        "19:00",
        120,
        50,
    )

    assert resultado == pelicula
    repo_mock.create.assert_called_once_with(
        "CINE001",
        "Película de prueba",
        "Acción",
        "19:00",
        120,
        50,
    )


def test_crear_pelicula_con_codigo_existente(servicio, repo_mock, pelicula):
    repo_mock.find_by_code.return_value = pelicula

    with pytest.raises(ValueError, match="Ya existe una película"):
        servicio.crear_pelicula("CINE001", "Otra película", "Drama", "20:00", 90, 20)

    repo_mock.create.assert_not_called()


@pytest.mark.parametrize(
    "datos",
    [
        ("", "Película", "Drama", "19:00", 90, 20),
        ("CINE002", "", "Drama", "19:00", 90, 20),
        ("CINE002", "Película", "", "19:00", 90, 20),
        ("CINE002", "Película", "Drama", "25:00", 90, 20),
        ("CINE002", "Película", "Drama", "19:00", 0, 20),
        ("CINE002", "Película", "Drama", "19:00", -10, 20),
        ("CINE002", "Película", "Drama", "19:00", 90, -1),
        ("CINE002", "Película", "Drama", "19:00", 90, 2.5),
    ],
)
def test_crear_pelicula_con_datos_invalidos(servicio, repo_mock, datos):
    with pytest.raises(ValueError):
        servicio.crear_pelicula(*datos)

    repo_mock.create.assert_not_called()


def test_actualizar_pelicula(servicio, repo_mock, pelicula):
    pelicula_actualizada = {**pelicula, "nombre": "Nuevo nombre"}
    repo_mock.find_by_code.return_value = pelicula
    repo_mock.update.return_value = pelicula_actualizada

    resultado = servicio.actualizar_pelicula(
        "CINE001",
        {"nombre": " Nuevo nombre "},
    )

    assert resultado == pelicula_actualizada
    repo_mock.update.assert_called_once_with(
        "CINE001",
        {"nombre": "Nuevo nombre"},
    )


def test_actualizar_pelicula_inexistente(servicio, repo_mock):
    repo_mock.find_by_code.return_value = None

    resultado = servicio.actualizar_pelicula(
        "CINE999",
        {"nombre": "Nuevo nombre"},
    )

    assert resultado is None
    repo_mock.update.assert_not_called()


def test_actualizar_campo_no_permitido(servicio, repo_mock):
    with pytest.raises(ValueError, match="No se permite actualizar"):
        servicio.actualizar_pelicula(
            "CINE001",
            {"codigo": "OTRO"},
        )

    repo_mock.update.assert_not_called()


@pytest.mark.parametrize(
    "campos",
    [
        {"nombre": ""},
        {"genero": "  "},
        {"hora_funcion": "28:00"},
        {"duracion": 0},
        {"duracion": 90.5},
        {"entradas_disponibles": -1},
        {"entradas_disponibles": True},
    ],
)
def test_actualizar_con_datos_invalidos(servicio, repo_mock, pelicula, campos):
    repo_mock.find_by_code.return_value = pelicula

    with pytest.raises(ValueError):
        servicio.actualizar_pelicula("CINE001", campos)

    repo_mock.update.assert_not_called()


def test_eliminar_pelicula(servicio, repo_mock):
    repo_mock.delete.return_value = True

    resultado = servicio.eliminar_pelicula(" CINE001 ")

    assert resultado is True
    repo_mock.delete.assert_called_once_with("CINE001")


def test_eliminar_pelicula_con_codigo_vacio(servicio, repo_mock):
    with pytest.raises(ValueError, match="codigo"):
        servicio.eliminar_pelicula(" ")

    repo_mock.delete.assert_not_called()
