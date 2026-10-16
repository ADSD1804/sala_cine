from db.connection import get_client


class UsuarioRepository:

    CAMPOS_ACTUALIZABLES = {"nombre", "correo"}

    def __init__(self):
        self.client = get_client()

    def find_all(self):
        query = self.client.execute("""
            SELECT
                id,
                cedula,
                nombre,
                correo
            FROM usuarios
            """)

        return [dict(zip(query.columns, row)) for row in query.rows]

    def find_by_cedula(self, cedula):
        query = self.client.execute(
            """
            SELECT
                id,
                cedula,
                nombre,
                correo
            FROM usuarios
            WHERE cedula = ?
            """,
            [cedula],
        )

        if not query.rows:
            return None

        return dict(zip(query.columns, query.rows[0]))

    def create(self, cedula, nombre, correo):
        self.client.execute(
            """
            INSERT INTO usuarios
            (
                cedula,
                nombre,
                correo
            )
            VALUES (?, ?, ?)
            """,
            [cedula, nombre, correo],
        )

        return self.find_by_cedula(cedula)

    def update(self, cedula, campos):
        campos_validos = {
            key: value
            for key, value in campos.items()
            if key in self.CAMPOS_ACTUALIZABLES and value is not None
        }

        if not campos_validos:
            return None

        sets = ", ".join(f"{key} = ?" for key in campos_validos)

        valores = list(campos_validos.values())
        valores.append(cedula)

        self.client.execute(
            f"""
            UPDATE usuarios
            SET {sets}
            WHERE cedula = ?
            """,
            valores,
        )

        return self.find_by_cedula(cedula)

    def delete(self, cedula):
        usuario = self.find_by_cedula(cedula)

        if usuario is None:
            return False

        self.client.execute(
            """
            DELETE FROM usuarios
            WHERE cedula = ?
            """,
            [cedula],
        )

        return True
