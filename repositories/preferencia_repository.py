from db.connection import get_client


class PreferenciaRepository:

    def __init__(self):
        self.client = get_client()

    def find_all(self):
        query = self.client.execute(""" 
        SELECT *
        FROM preferencias
        """)

        return dict(zip(query.columns, query.rows[0]))

    def find_by_id(self, preferencia_id):
        query = self.client.execute(
            """
        SELECT *
            FROM preferencias
            WHERE id = ?
        """,
            [preferencia_id],
        )

        if not query.rows:
            return None

        return dict(zip(query.columns, query.rows[0]))

    def create(self, genero_pelicula):
        self.client.execute(
            """
            INSERT INTO preferencias (genero_pelicula)
            VALUES (?)
            """,
            [genero_pelicula],
        )
        query = self.client.execute(
            """
            SELECT *
            FROM preferencias
            WHERE genero_pelicula = ?
            """,
            [genero_pelicula],
        )

        return dict(zip(query.columns, query.rows[0]))

    def update(self, preferencia_id, genero_pelicula):
        self.client.execute(
            """
            UPDATE preferencias
            SET genero_pelicula = ?
            WHERE id = ?
            """,
            [genero_pelicula, preferencia_id],
        )

    def delete(self, preferencia_id):
        self.client.execute(
            """
            DELETE FROM preferencias
            WHERE id = ?
            """,
            [preferencia_id],
        )
