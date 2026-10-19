from repositories.usuario_repository import UsuarioRepository


class UsuarioService:

    def __init__(self, usuario_repository=None):
        self.usuario_repository = (
            usuario_repository
            if usuario_repository is not None
            else UsuarioRepository()
        )

    def listar_usuarios(self):
        return self.usuario_repository.find_all()

    def buscar_por_cedula(self, cedula):
        if not cedula or not str(cedula).strip():
            raise ValueError("La cédula es obligatoria.")

        return self.usuario_repository.find_by_cedula(str(cedula).strip())

    def crear_usuario(self, cedula, nombre, correo):
        cedula = str(cedula).strip() if cedula is not None else ""
        nombre = nombre.strip() if isinstance(nombre, str) else ""
        correo = correo.strip() if isinstance(correo, str) else ""

        if not cedula:
            raise ValueError("La cédula es obligatoria.")

        if not nombre:
            raise ValueError("El nombre es obligatorio.")

        if not correo:
            raise ValueError("El correo es obligatorio.")

        if "@" not in correo or "." not in correo.split("@")[-1]:
            raise ValueError("El correo electrónico no es válido.")

        usuario_existente = self.usuario_repository.find_by_cedula(cedula)

        if usuario_existente is not None:
            raise ValueError("Ya existe un usuario con esa cédula.")

        return self.usuario_repository.create(
            cedula,
            nombre,
            correo,
        )

    def actualizar_usuario(self, cedula, campos):
        if not cedula or not str(cedula).strip():
            raise ValueError("La cédula es obligatoria.")

        if not isinstance(campos, dict) or not campos:
            raise ValueError("Debes indicar los campos que deseas actualizar.")

        cedula = str(cedula).strip()
        campos_permitidos = {"nombre", "correo"}

        campos_invalidos = set(campos) - campos_permitidos
        if campos_invalidos:
            raise ValueError(
                f"No se permite actualizar estos campos: "
                f"{', '.join(sorted(campos_invalidos))}."
            )

        campos_limpios = {}

        for campo, valor in campos.items():
            if not isinstance(valor, str) or not valor.strip():
                raise ValueError(f"El campo '{campo}' no puede estar vacío.")

            valor = valor.strip()

            if campo == "correo":
                if "@" not in valor or "." not in valor.split("@")[-1]:
                    raise ValueError("El correo electrónico no es válido.")

            campos_limpios[campo] = valor

        usuario = self.usuario_repository.find_by_cedula(cedula)

        if usuario is None:
            return None

        return self.usuario_repository.update(cedula, campos_limpios)

    def eliminar_usuario(self, cedula):
        if not cedula or not str(cedula).strip():
            raise ValueError("La cédula es obligatoria.")

        return self.usuario_repository.delete(str(cedula).strip())
