import pytest
from unittest.mock import Mock

from services.preferencia_service import PreferenciaService


@pytest.fixture
def repo_mock():
    return Mock()


@pytest.fixture
def servicio(repo_mock):
    return PreferenciaService(preferencia_repository=repo_mock)


@pytest.fixture
def preferencia():
    return {
        "id": 1,
        "genero_pelicula": "Terror",
    }


def test_listar_preferencias(servicio, repo_mock, preferencia):
    repo_mock.find_all.return_value = preferencia

    resultado = servicio.listar_preferencias()

    assert resultado == preferencia
    repo_mock.find_all.assert_called_once_with()


def test_buscar_por_id(servicio, repo_mock, preferencia):
    repo_mock.find_by_id.return_value = preferencia

    resultado = servicio.buscar_por_id(1)

    assert resultado == preferencia
    repo_mock.find_by_id.assert_called_once_with(1)


@pytest.mark.parametrize("preferencia_id", [0, -1, "1", None, True])
def test_buscar_por_id_invalido(servicio, repo_mock, preferencia_id):
    with pytest.raises(ValueError, match="ID de la preferencia"):
        servicio.buscar_por_id(preferencia_id)

    repo_mock.find_by_id.assert_not_called()


def test_crear_preferencia(servicio, repo_mock, preferencia):
    repo_mock.create.return_value = preferencia

    resultado = servicio.crear_preferencia(" Terror ")

    assert resultado == preferencia
    repo_mock.create.assert_called_once_with("Terror")


@pytest.mark.parametrize(
    "genero",
    ["", "   ", None, 123],
)
def test_crear_preferencia_con_genero_invalido(servicio, repo_mock, genero):
    with pytest.raises(ValueError, match="género de película"):
        servicio.crear_preferencia(genero)

    repo_mock.create.assert_not_called()


def test_actualizar_preferencia(servicio, repo_mock, preferencia):
    preferencia_actualizada = {
        "id": 1,
        "genero_pelicula": "Romance",
    }

    repo_mock.find_by_id.side_effect = [
        preferencia,
        preferencia_actualizada,
    ]

    resultado = servicio.actualizar_preferencia(1, " Romance ")

    assert resultado == preferencia_actualizada
    repo_mock.update.assert_called_once_with(1, "Romance")
    assert repo_mock.find_by_id.call_count == 2


def test_actualizar_preferencia_inexistente(servicio, repo_mock):
    repo_mock.find_by_id.return_value = None

    resultado = servicio.actualizar_preferencia(99, "Romance")

    assert resultado is None
    repo_mock.update.assert_not_called()


def test_actualizar_preferencia_con_genero_vacio(servicio, repo_mock):
    with pytest.raises(ValueError):
        servicio.actualizar_preferencia(1, " ")

    repo_mock.find_by_id.assert_not_called()
    repo_mock.update.assert_not_called()


def test_eliminar_preferencia(servicio, repo_mock, preferencia):
    repo_mock.find_by_id.return_value = preferencia

    resultado = servicio.eliminar_preferencia(1)

    assert resultado is True
    repo_mock.delete.assert_called_once_with(1)


def test_eliminar_preferencia_inexistente(servicio, repo_mock):
    repo_mock.find_by_id.return_value = None

    resultado = servicio.eliminar_preferencia(99)

    assert resultado is False
    repo_mock.delete.assert_not_called()
