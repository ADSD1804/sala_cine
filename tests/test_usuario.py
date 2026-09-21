from repositories.usuario_repository import UsuarioRepository

def test_crear_usuarios():

    repo = UsuarioRepository()

    cedula = "123456789"

    usuario = repo.create(
        cedula,
        "Usuario de prueba2",
        "prueba2@test.com",
    )

    assert usuario is not None
    assert usuario["cedula"] == cedula
    assert usuario["nombre"] == "Usuario de prueba2"
    assert usuario["correo"] == "prueba2@test.com"

    repo.delete(cedula)

def test_buscar_usuario_cedula():
    repo = UsuarioRepository()

    cedula = "99999999"

    repo.create(cedula, "Usuario prueba buscar", "prueba@encontrartest.com")

    usuario = repo.find_by_cedula(cedula)

    assert usuario is not None
    assert usuario["cedula"] == cedula
    assert usuario["nombre"] == "Usuario prueba buscar"

    repo.delete(cedula)

def test_actualizar_usuario():

    repo = UsuarioRepository()

    cedula = "12344567"

    repo.create(cedula, "Usuario a actualizar", "usuario@update.com")

    usuario_actualizado = repo.update(
        cedula,
        {"nombre": "Usuario actualizado", "correo": "correo@actualizado.com"},
    )

    assert usuario_actualizado is not None
    assert usuario_actualizado["cedula"] == cedula
    assert usuario_actualizado["nombre"] == "Usuario actualizado"
    assert usuario_actualizado["correo"] == "correo@actualizado.com"

    repo.delete(cedula)

def test_delete_usuario():
    repo = UsuarioRepository()
    
    cedula = "100322214"
    
    repo.create(cedula, "Usuario a eliminar", "usuario@delete.com")
    
    usuario_eliminado = repo.delete(cedula)
    
    assert usuario_eliminado is True
    assert repo.find_by_cedula(cedula) is None