from repositories.preferencia_repository import PreferenciaRepository
from repositories.usuario_repository import UsuarioRepository
from repositories.usuario_preferencia_repository import UsuarioPreferenciaRepository

repoPreferencia = PreferenciaRepository()
repoUsuario = UsuarioRepository()
repoUsuarioPreferencia = UsuarioPreferenciaRepository()


def test_agregar_preferencia():
    cedula = "TEST_REL_001"
    correo = "test_rel_001@example.com"
    genero = "Terror"

    usuario = None
    preferencia = None

    try:
        usuario = repoUsuario.create(cedula, "Usuario Prueba", correo)
        preferencia = repoPreferencia.create(genero)

        resultado = repoUsuarioPreferencia.agregar_preferencia(
            cedula, preferencia["id"]
        )

        assert resultado is not None
        assert resultado["usuario_cedula"] == cedula
        assert resultado["preferencia_id"] == preferencia["id"]
        assert repoUsuarioPreferencia.existe(cedula, preferencia["id"]) is True

    finally:
        if preferencia is not None:
            repoUsuarioPreferencia.eliminar_preferencia(cedula, preferencia["id"])
            repoPreferencia.delete(preferencia["id"])

        if usuario is not None:
            repoUsuario.delete(cedula)


def test_buscar_preferencia_por_usuario():
    cedula = "TEST_REL_002"
    correo = "test_rel_002@example.com"

    usuario = None
    preferencias = []

    try:
        usuario = repoUsuario.create(cedula, "Usuario Prueba", correo)

        for genero in ["Accion", "Comedia"]:
            preferencias.append(repoPreferencia.create(genero))

        for preferencia in preferencias:
            repoUsuarioPreferencia.agregar_preferencia(cedula, preferencia["id"])

        resultado = repoUsuarioPreferencia.find_by_usuario(cedula)

        assert resultado is not None
        assert resultado["usuario_cedula"] == cedula
        assert resultado["preferencia_id"] in [p["id"] for p in preferencias]

    finally:
        for preferencia in preferencias:
            repoUsuarioPreferencia.eliminar_preferencia(cedula, preferencia["id"])
            repoPreferencia.delete(preferencia["id"])

        if usuario is not None:
            repoUsuario.delete(cedula)


def test_buscar_usuario_por_preferencia():
    cedula = "TEST_REL_003"
    correo = "test_rel_003@example.com"
    genero = "Suspenso"

    usuario = None
    preferencia = None

    try:
        usuario = repoUsuario.create(cedula, "Usuario Prueba", correo)
        preferencia = repoPreferencia.create(genero)

        repoUsuarioPreferencia.agregar_preferencia(cedula, preferencia["id"])

        resultado = repoUsuarioPreferencia.find_by_preferencia(preferencia["id"])

        assert resultado is not None
        assert resultado["usuario_cedula"] == cedula
        assert resultado["preferencia_id"] == preferencia["id"]

    finally:
        if preferencia is not None:
            repoUsuarioPreferencia.eliminar_preferencia(cedula, preferencia["id"])
            repoPreferencia.delete(preferencia["id"])

        if usuario is not None:
            repoUsuario.delete(cedula)


def test_verificar_existencia_relacion():
    cedula = "TEST_REL_004"
    correo = "test_rel_004@example.com"
    genero = "Drama"

    usuario = None
    preferencia = None

    try:
        usuario = repoUsuario.create(cedula, "Usuario Prueba", correo)
        preferencia = repoPreferencia.create(genero)

        assert repoUsuarioPreferencia.existe(cedula, preferencia["id"]) is False

        repoUsuarioPreferencia.agregar_preferencia(cedula, preferencia["id"])

        assert repoUsuarioPreferencia.existe(cedula, preferencia["id"]) is True

    finally:
        if preferencia is not None:
            repoUsuarioPreferencia.eliminar_preferencia(cedula, preferencia["id"])
            repoPreferencia.delete(preferencia["id"])

        if usuario is not None:
            repoUsuario.delete(cedula)


def test_eliminar_preferencia_asignada():
    cedula = "TEST_REL_005"
    correo = "test_rel_005@example.com"
    genero = "Romance"

    usuario = None
    preferencia = None

    try:
        usuario = repoUsuario.create(cedula, "Usuario Prueba", correo)
        preferencia = repoPreferencia.create(genero)

        repoUsuarioPreferencia.agregar_preferencia(cedula, preferencia["id"])

        assert repoUsuarioPreferencia.existe(cedula, preferencia["id"]) is True

        repoUsuarioPreferencia.eliminar_preferencia(cedula, preferencia["id"])

        assert repoUsuarioPreferencia.existe(cedula, preferencia["id"]) is False

        # Eliminar la relación no debe borrar las entidades originales.
        assert repoUsuario.find_by_cedula(cedula) is not None
        assert repoPreferencia.find_by_id(preferencia["id"]) is not None

    finally:
        if preferencia is not None:
            repoUsuarioPreferencia.eliminar_preferencia(cedula, preferencia["id"])
            repoPreferencia.delete(preferencia["id"])

        if usuario is not None:
            repoUsuario.delete(cedula)
