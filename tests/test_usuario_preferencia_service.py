import pytest
from unittest.mock import Mock

from services.usuario_preferencia_service import UsuarioPreferenciaService


@pytest.fixture
def repo_relacion():
    return Mock()


@pytest.fixture
def repo_usuario():
    return Mock()


@pytest.fixture
def repo_preferencia():
    return Mock()


@pytest.fixture
def servicio(repo_relacion, repo_usuario, repo_preferencia):
    return UsuarioPreferenciaService(
        usuario_preferencia_repository=repo_relacion,
        usuario_repository=repo_usuario,
        preferencia_repository=repo_preferencia,
    )


@pytest.fixture
def relacion():
    return {
        "usuario_cedula": "123456",
        "preferencia_id": 1,
    }


def configurar_entidades_existentes(repo_usuario, repo_preferencia):
    repo_usuario.find_by_cedula.return_value = {
        "cedula": "123456",
        "nombre": "Carlos",
        "correo": "carlos@test.com",
    }
    repo_preferencia.find_by_id.return_value = {
        "id": 1,
        "genero_pelicula": "Terror",
    }


def test_agregar_preferencia(
    servicio,
    repo_relacion,
    repo_usuario,
    repo_preferencia,
    relacion,
):
    configurar_entidades_existentes(repo_usuario, repo_preferencia)
    repo_relacion.existe.return_value = False
    repo_relacion.agregar_preferencia.return_value = relacion

    resultado = servicio.agregar_preferencia(" 123456 ", 1)

    assert resultado == relacion
    repo_usuario.find_by_cedula.assert_called_once_with("123456")
    repo_preferencia.find_by_id.assert_called_once_with(1)
    repo_relacion.agregar_preferencia.assert_called_once_with("123456", 1)


def test_agregar_preferencia_usuario_inexistente(servicio, repo_relacion, repo_usuario):
    repo_usuario.find_by_cedula.return_value = None

    with pytest.raises(ValueError, match="El usuario no existe"):
        servicio.agregar_preferencia("123456", 1)

    repo_relacion.agregar_preferencia.assert_not_called()


def test_agregar_preferencia_genero_inexistente(
    servicio, repo_relacion, repo_usuario, repo_preferencia
):
    repo_usuario.find_by_cedula.return_value = {"cedula": "123456"}
    repo_preferencia.find_by_id.return_value = None

    with pytest.raises(ValueError, match="La preferencia no existe"):
        servicio.agregar_preferencia("123456", 1)

    repo_relacion.agregar_preferencia.assert_not_called()


def test_agregar_preferencia_duplicada(
    servicio, repo_relacion, repo_usuario, repo_preferencia
):
    configurar_entidades_existentes(repo_usuario, repo_preferencia)
    repo_relacion.existe.return_value = True

    with pytest.raises(ValueError, match="ya tiene asignada"):
        servicio.agregar_preferencia("123456", 1)

    repo_relacion.agregar_preferencia.assert_not_called()


@pytest.mark.parametrize(
    "cedula,preferencia_id",
    [
        ("", 1),
        ("   ", 1),
        (None, 1),
        ("123456", 0),
        ("123456", -1),
        ("123456", "1"),
        ("123456", True),
    ],
)
def test_agregar_preferencia_datos_invalidos(
    servicio, repo_relacion, cedula, preferencia_id
):
    with pytest.raises(ValueError):
        servicio.agregar_preferencia(cedula, preferencia_id)

    repo_relacion.agregar_preferencia.assert_not_called()


def test_buscar_por_usuario(servicio, repo_relacion, relacion):
    repo_relacion.find_by_usuario.return_value = relacion

    resultado = servicio.buscar_por_usuario(" 123456 ")

    assert resultado == relacion
    repo_relacion.find_by_usuario.assert_called_once_with("123456")


def test_buscar_por_preferencia(servicio, repo_relacion, relacion):
    repo_relacion.find_by_preferencia.return_value = relacion

    resultado = servicio.buscar_por_preferencia(1)

    assert resultado == relacion
    repo_relacion.find_by_preferencia.assert_called_once_with(1)


def test_existe_relacion(servicio, repo_relacion):
    repo_relacion.existe.return_value = True

    resultado = servicio.existe_relacion("123456", 1)

    assert resultado is True
    repo_relacion.existe.assert_called_once_with("123456", 1)


def test_eliminar_preferencia_asignada(servicio, repo_relacion):
    repo_relacion.existe.return_value = True

    resultado = servicio.eliminar_preferencia("123456", 1)

    assert resultado is True
    repo_relacion.eliminar_preferencia.assert_called_once_with("123456", 1)


def test_eliminar_relacion_inexistente(servicio, repo_relacion):
    repo_relacion.existe.return_value = False

    resultado = servicio.eliminar_preferencia("123456", 1)

    assert resultado is False
    repo_relacion.eliminar_preferencia.assert_not_called()


def test_buscar_por_usuario_con_cedula_vacia(servicio, repo_relacion):
    with pytest.raises(ValueError, match="cédula"):
        servicio.buscar_por_usuario(" ")

    repo_relacion.find_by_usuario.assert_not_called()


def test_buscar_por_preferencia_con_id_invalido(servicio, repo_relacion):
    with pytest.raises(ValueError, match="ID de la preferencia"):
        servicio.buscar_por_preferencia(-1)

    repo_relacion.find_by_preferencia.assert_not_called()
