from repositories.preferencia_repository import PreferenciaRepository


class PreferenciaService:

    def __init__(self, preferencia_repository=None):
        self.preferencia_repository = (
            preferencia_repository
            if preferencia_repository is not None
            else PreferenciaRepository()
        )

    @staticmethod
    def _validar_genero(genero_pelicula):
        if not isinstance(genero_pelicula, str) or not genero_pelicula.strip():
            raise ValueError("El género de película es obligatorio.")

        return genero_pelicula.strip()

    @staticmethod
    def _validar_id(preferencia_id):
        if (
            isinstance(preferencia_id, bool)
            or not isinstance(preferencia_id, int)
            or preferencia_id <= 0
        ):
            raise ValueError("El ID de la preferencia debe ser un entero positivo.")

        return preferencia_id

    def listar_preferencias(self):
        return self.preferencia_repository.find_all()

    def buscar_por_id(self, preferencia_id):
        preferencia_id = self._validar_id(preferencia_id)

        return self.preferencia_repository.find_by_id(preferencia_id)

    def crear_preferencia(self, genero_pelicula):
        genero_pelicula = self._validar_genero(genero_pelicula)

        return self.preferencia_repository.create(genero_pelicula)

    def actualizar_preferencia(self, preferencia_id, genero_pelicula):
        preferencia_id = self._validar_id(preferencia_id)
        genero_pelicula = self._validar_genero(genero_pelicula)

        preferencia = self.preferencia_repository.find_by_id(preferencia_id)

        if preferencia is None:
            return None

        self.preferencia_repository.update(
            preferencia_id,
            genero_pelicula,
        )

        return self.preferencia_repository.find_by_id(preferencia_id)

    def eliminar_preferencia(self, preferencia_id):
        preferencia_id = self._validar_id(preferencia_id)

        preferencia = self.preferencia_repository.find_by_id(preferencia_id)

        if preferencia is None:
            return False

        self.preferencia_repository.delete(preferencia_id)

        return True
