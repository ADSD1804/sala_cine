import math

from repositories.compra_repository import CompraRepository
from repositories.usuario_repository import UsuarioRepository
from repositories.pelicula_repository import PeliculaRepository


class CompraService:
    def __init__(
        self,
        compra_repository=None,
        usuario_repository=None,
        pelicula_repository=None,
    ):
        self.compra_repository = (
            compra_repository if compra_repository is not None else CompraRepository()
        )
        self.usuario_repository = (
            usuario_repository
            if usuario_repository is not None
            else UsuarioRepository()
        )
        self.pelicula_repository = (
            pelicula_repository
            if pelicula_repository is not None
            else PeliculaRepository()
        )

    @staticmethod
    def _validar_texto(valor, campo):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"{campo} es obligatorio.")
        return valor.strip()

    @staticmethod
    def _validar_id(compra_id):
        if (
            isinstance(compra_id, bool)
            or not isinstance(compra_id, int)
            or compra_id <= 0
        ):
            raise ValueError("El ID de la compra debe ser un entero positivo.")
        return compra_id

    @staticmethod
    def _validar_cantidad(cantidad):
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo.")
        return cantidad

    @staticmethod
    def _validar_total(total):
        if (
            isinstance(total, bool)
            or not isinstance(total, (int, float))
            or not math.isfinite(total)
            or total < 0
        ):
            raise ValueError("El total debe ser un número válido no negativo.")
        return total

    def listar_compras(self):
        return self.compra_repository.find_all()

    def buscar_por_id(self, compra_id):
        compra_id = self._validar_id(compra_id)
        return self.compra_repository.find_by_id(compra_id)

    def buscar_por_usuario(self, usuario_cedula):
        usuario_cedula = self._validar_texto(usuario_cedula, "La cédula del usuario")
        return self.compra_repository.find_by_usuario(usuario_cedula)

    def buscar_por_pelicula(self, pelicula_codigo):
        pelicula_codigo = self._validar_texto(
            pelicula_codigo, "El código de la película"
        )
        return self.compra_repository.find_by_pelicula(pelicula_codigo)

    def crear_compra(self, usuario_cedula, pelicula_codigo, cantidad, total):
        usuario_cedula = self._validar_texto(usuario_cedula, "La cédula del usuario")
        pelicula_codigo = self._validar_texto(
            pelicula_codigo, "El código de la película"
        )
        cantidad = self._validar_cantidad(cantidad)
        total = self._validar_total(total)

        usuario = self.usuario_repository.find_by_cedula(usuario_cedula)
        if usuario is None:
            raise ValueError("No existe un usuario con esa cédula.")

        pelicula = self.pelicula_repository.find_by_code(pelicula_codigo)
        if pelicula is None:
            raise ValueError("No existe una película con ese código.")

        return self.compra_repository.create(
            usuario_cedula,
            pelicula_codigo,
            cantidad,
            total,
        )

    def eliminar_compra(self, compra_id):
        compra_id = self._validar_id(compra_id)
        return self.compra_repository.delete(compra_id)
