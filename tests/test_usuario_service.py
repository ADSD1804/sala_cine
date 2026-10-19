import pytest
from unittest.mock import Mock

from services.usuario_service import UsuarioService


@pytest.fixture
def repo_mock():
    return Mock()


@pytest.fixture
def servicio(repo_mock):
    return UsuarioService(usuario_repository=repo_mock)


def test_listar_usuarios(servicio, repo_mock):
    usuarios = [
        {
            "cedula": "123",
            "nombre": "Carlos",
            "correo": "carlos@test.com",
        }
    ]
    repo_mock.find_all.return_value = usuarios

    resultado = servicio.listar_usuarios()

    assert resultado == usuarios
    repo_mock.find_all.assert_called_once_with()


def test_buscar_por_cedula(servicio, repo_mock):
    usuario = {
        "cedula": "123",
        "nombre": "Carlos",
        "correo": "carlos@test.com",
    }
    repo_mock.find_by_cedula.return_value = usuario

    resultado = servicio.buscar_por_cedula(" 123 ")

    assert resultado == usuario
    repo_mock.find_by_cedula.assert_called_once_with("123")


def test_buscar_por_cedula_vacia(servicio, repo_mock):
    with pytest.raises(ValueError, match="cédula es obligatoria"):
        servicio.buscar_por_cedula(" ")

    repo_mock.find_by_cedula.assert_not_called()


def test_crear_usuario(servicio, repo_mock):
    usuario = {
        "cedula": "123",
        "nombre": "Carlos",
        "correo": "carlos@test.com",
    }
    repo_mock.find_by_cedula.return_value = None
    repo_mock.create.return_value = usuario

    resultado = servicio.crear_usuario(
        " 123 ",
        " Carlos ",
        " carlos@test.com ",
    )

    assert resultado == usuario
    repo_mock.create.assert_called_once_with(
        "123",
        "Carlos",
        "carlos@test.com",
    )


def test_crear_usuario_con_cedula_existente(servicio, repo_mock):
    repo_mock.find_by_cedula.return_value = {
        "cedula": "123",
        "nombre": "Carlos",
        "correo": "carlos@test.com",
    }

    with pytest.raises(ValueError, match="Ya existe un usuario"):
        servicio.crear_usuario("123", "Ana", "ana@test.com")

    repo_mock.create.assert_not_called()


@pytest.mark.parametrize(
    "cedula,nombre,correo",
    [
        ("", "Carlos", "carlos@test.com"),
        ("123", "", "carlos@test.com"),
        ("123", "Carlos", ""),
        ("123", "Carlos", "correo-invalido"),
    ],
)
def test_crear_usuario_con_datos_invalidos(servicio, repo_mock, cedula, nombre, correo):
    with pytest.raises(ValueError):
        servicio.crear_usuario(cedula, nombre, correo)

    repo_mock.create.assert_not_called()


def test_actualizar_usuario(servicio, repo_mock):
    usuario = {
        "cedula": "123",
        "nombre": "Carlos",
        "correo": "carlos@test.com",
    }
    usuario_actualizado = {
        "cedula": "123",
        "nombre": "Carlos Pérez",
        "correo": "carlos@test.com",
    }

    repo_mock.find_by_cedula.return_value = usuario
    repo_mock.update.return_value = usuario_actualizado

    resultado = servicio.actualizar_usuario(
        "123",
        {"nombre": " Carlos Pérez "},
    )

    assert resultado == usuario_actualizado
    repo_mock.update.assert_called_once_with(
        "123",
        {"nombre": "Carlos Pérez"},
    )


def test_actualizar_usuario_inexistente(servicio, repo_mock):
    repo_mock.find_by_cedula.return_value = None

    resultado = servicio.actualizar_usuario(
        "123",
        {"nombre": "Carlos Pérez"},
    )

    assert resultado is None
    repo_mock.update.assert_not_called()


def test_actualizar_usuario_con_campo_no_permitido(servicio, repo_mock):
    with pytest.raises(ValueError, match="No se permite actualizar"):
        servicio.actualizar_usuario(
            "123",
            {"cedula": "456"},
        )

    repo_mock.update.assert_not_called()


def test_eliminar_usuario(servicio, repo_mock):
    repo_mock.delete.return_value = True

    resultado = servicio.eliminar_usuario(" 123 ")

    assert resultado is True
    repo_mock.delete.assert_called_once_with("123")


def test_eliminar_usuario_inexistente(servicio, repo_mock):
    repo_mock.delete.return_value = False

    resultado = servicio.eliminar_usuario("123")

    assert resultado is False
