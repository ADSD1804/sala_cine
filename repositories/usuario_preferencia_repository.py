from db.connection import get_client


class UsuarioPreferenciaRepository:

    def __init__(self):
        self.client = get_client()

    def agregar_preferencia(self, usuario_cedula, preferencia_id):
        self.client.execute(
            """
            INSERT INTO usuario_preferencias (usuario_cedula, preferencia_id)
            VALUES (?, ?)
            """,
            [usuario_cedula, preferencia_id],
        )
        query = self.client.execute(
            """
            SELECT *
            FROM usuario_preferencias
            WHERE usuario_cedula = ? AND preferencia_id = ?
            """,
            [usuario_cedula, preferencia_id],
        )

        if not query.rows:
            return None

        return dict(zip(query.columns, query.rows[0]))

    def eliminar_preferencia(self, usuario_cedula, preferencia_id):
        self.client.execute(
            """
            DELETE FROM usuario_preferencias
            WHERE usuario_cedula = ? AND preferencia_id = ?
            """,
            [usuario_cedula, preferencia_id],
        )

    def find_by_usuario(self, usuario_cedula):
        query = self.client.execute(
            """
            SELECT *
            FROM usuario_preferencias
            WHERE usuario_cedula = ?
            """,
            [usuario_cedula],
        )

        if not query.rows:
            return None

        return dict(zip(query.columns, query.rows[0]))

    def find_by_preferencia(self, preferencia_id):
        query = self.client.execute(
            """
            SELECT *
            FROM usuario_preferencias
            WHERE preferencia_id = ?
            """,
            [preferencia_id],
        )

        if not query.rows:
            return None

        return dict(zip(query.columns, query.rows[0]))

    def existe(self, usuario_cedula, preferencia_id):
        query = self.client.execute(
            """
            SELECT *
            FROM usuario_preferencias
            WHERE usuario_cedula = ? AND preferencia_id = ?
            """,
            [usuario_cedula, preferencia_id],
        )

        return bool(query.rows)
