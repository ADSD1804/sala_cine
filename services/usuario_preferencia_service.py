from repositories.usuario_preferencia_repository import UsuarioPreferenciaRepository
from repositories.usuario_repository import UsuarioRepository
from repositories.preferencia_repository import PreferenciaRepository


class UsuarioPreferenciaService:

    def __init__(
        self,
        usuario_preferencia_repository=None,
        usuario_repository=None,
        preferencia_repository=None,
    ):
        self.usuario_preferencia_repository = (
            usuario_preferencia_repository
            if usuario_preferencia_repository is not None
            else UsuarioPreferenciaRepository()
        )

        self.usuario_repository = (
            usuario_repository
            if usuario_repository is not None
            else UsuarioRepository()
        )

        self.preferencia_repository = (
            preferencia_repository
            if preferencia_repository is not None
            else PreferenciaRepository()
        )

    @staticmethod
    def _validar_cedula(usuario_cedula):
        if not isinstance(usuario_cedula, str) or not usuario_cedula.strip():
            raise ValueError("La cédula del usuario es obligatoria.")

        return usuario_cedula.strip()

    @staticmethod
    def _validar_preferencia_id(preferencia_id):
        if (
            isinstance(preferencia_id, bool)
            or not isinstance(preferencia_id, int)
            or preferencia_id <= 0
        ):
            raise ValueError("El ID de la preferencia debe ser un entero positivo.")

        return preferencia_id

    def agregar_preferencia(self, usuario_cedula, preferencia_id):
        usuario_cedula = self._validar_cedula(usuario_cedula)
        preferencia_id = self._validar_preferencia_id(preferencia_id)

        usuario = self.usuario_repository.find_by_cedula(usuario_cedula)

        if usuario is None:
            raise ValueError("El usuario no existe.")

        preferencia = self.preferencia_repository.find_by_id(preferencia_id)

        if preferencia is None:
            raise ValueError("La preferencia no existe.")

        if self.usuario_preferencia_repository.existe(usuario_cedula, preferencia_id):
            raise ValueError("El usuario ya tiene asignada esa preferencia.")

        return self.usuario_preferencia_repository.agregar_preferencia(
            usuario_cedula,
            preferencia_id,
        )

    def eliminar_preferencia(self, usuario_cedula, preferencia_id):
        usuario_cedula = self._validar_cedula(usuario_cedula)
        preferencia_id = self._validar_preferencia_id(preferencia_id)

        existe_relacion = self.usuario_preferencia_repository.existe(
            usuario_cedula,
            preferencia_id,
        )

        if not existe_relacion:
            return False

        self.usuario_preferencia_repository.eliminar_preferencia(
            usuario_cedula,
            preferencia_id,
        )

        return True

    def buscar_por_usuario(self, usuario_cedula):
        usuario_cedula = self._validar_cedula(usuario_cedula)

        return self.usuario_preferencia_repository.find_by_usuario(usuario_cedula)

    def buscar_por_preferencia(self, preferencia_id):
        preferencia_id = self._validar_preferencia_id(preferencia_id)

        return self.usuario_preferencia_repository.find_by_preferencia(preferencia_id)

    def existe_relacion(self, usuario_cedula, preferencia_id):
        usuario_cedula = self._validar_cedula(usuario_cedula)
        preferencia_id = self._validar_preferencia_id(preferencia_id)

        return self.usuario_preferencia_repository.existe(
            usuario_cedula,
            preferencia_id,
        )
