from datetime import datetime

from repositories.pelicula_repository import PeliculaRepository


class PeliculaService:

    CAMPOS_ACTUALIZABLES = {
        "nombre",
        "genero",
        "hora_funcion",
        "duracion",
        "entradas_disponibles",
    }

    def __init__(self, pelicula_repository=None):
        self.pelicula_repository = (
            pelicula_repository
            if pelicula_repository is not None
            else PeliculaRepository()
        )

    @staticmethod
    def _validar_texto(valor, campo):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"El campo '{campo}' es obligatorio.")

        return valor.strip()

    @staticmethod
    def _validar_hora(hora_funcion):
        if not isinstance(hora_funcion, str):
            raise ValueError("La hora de función debe tener el formato HH:MM.")

        try:
            hora = datetime.strptime(hora_funcion.strip(), "%H:%M")
        except ValueError:
            raise ValueError(
                "La hora de función debe tener el formato HH:MM."
            ) from None

        if hora.strftime("%H:%M") != hora_funcion.strip():
            raise ValueError("La hora de función debe tener el formato HH:MM.")

        return hora_funcion.strip()

    @staticmethod
    def _validar_entero(valor, campo, minimo):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise ValueError(f"El campo '{campo}' debe ser un número entero.")

        if valor < minimo:
            raise ValueError(f"El campo '{campo}' debe ser como mínimo {minimo}.")

        return valor

    def listar_peliculas(self):
        return self.pelicula_repository.find_all()

    def buscar_por_codigo(self, codigo):
        codigo = self._validar_texto(codigo, "codigo")
        return self.pelicula_repository.find_by_code(codigo)

    def crear_pelicula(
        self,
        codigo,
        nombre,
        genero,
        hora_funcion,
        duracion,
        entradas_disponibles,
    ):
        codigo = self._validar_texto(codigo, "codigo")
        nombre = self._validar_texto(nombre, "nombre")
        genero = self._validar_texto(genero, "genero")
        hora_funcion = self._validar_hora(hora_funcion)
        duracion = self._validar_entero(duracion, "duracion", 1)
        entradas_disponibles = self._validar_entero(
            entradas_disponibles,
            "entradas_disponibles",
            0,
        )

        existente = self.pelicula_repository.find_by_code(codigo)

        if existente is not None:
            raise ValueError("Ya existe una película con ese código.")

        return self.pelicula_repository.create(
            codigo,
            nombre,
            genero,
            hora_funcion,
            duracion,
            entradas_disponibles,
        )

    def actualizar_pelicula(self, codigo, campos):
        codigo = self._validar_texto(codigo, "codigo")

        if not isinstance(campos, dict) or not campos:
            raise ValueError("Debes indicar los campos que deseas actualizar.")

        campos_invalidos = set(campos) - self.CAMPOS_ACTUALIZABLES

        if campos_invalidos:
            raise ValueError(
                "No se permite actualizar estos campos: "
                f"{', '.join(sorted(campos_invalidos))}."
            )

        pelicula = self.pelicula_repository.find_by_code(codigo)

        if pelicula is None:
            return None

        campos_limpios = {}

        for campo, valor in campos.items():
            if campo in {"nombre", "genero"}:
                campos_limpios[campo] = self._validar_texto(valor, campo)

            elif campo == "hora_funcion":
                campos_limpios[campo] = self._validar_hora(valor)

            elif campo == "duracion":
                campos_limpios[campo] = self._validar_entero(valor, campo, 1)

            elif campo == "entradas_disponibles":
                campos_limpios[campo] = self._validar_entero(valor, campo, 0)

        return self.pelicula_repository.update(codigo, campos_limpios)

    def eliminar_pelicula(self, codigo):
        codigo = self._validar_texto(codigo, "codigo")
        return self.pelicula_repository.delete(codigo)
