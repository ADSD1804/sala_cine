from db.connection import getClient

class PeliculaRepository:

    CAMPOS_ACTUALIZABLES = {
        "nombre",
        "genero",
        "hora_funcion",
        "duracion",
        "entradas_disponibles"
    }

    def __init__(self):
        self.client = getClient()

    def find_all(self):
        query = self.client.execute(
            """
            SELECT
                id,
                nombre,
                genero,
                hora_funcion,
                duracion,
                entradas_disponibles
            FROM peliculas
            """
        )

        return [
            dict(zip(query.columns, row))
            for row in query.rows
        ]

    def find_by_id(self, id):
        query = self.client.execute(
            """
            SELECT
                id,
                nombre,
                genero,
                hora_funcion,
                duracion,
                entradas_disponibles
            FROM peliculas
            WHERE id = ?
            """,
            [id]
        )

        if not query.rows:
            return None

        return dict(zip(query.columns, query.rows[0]))

    def create(
        self,
        nombre,
        genero,
        hora_funcion,
        duracion,
        entradas_disponibles
    ):

        query = self.client.execute(
            """
            INSERT INTO peliculas
            (
                nombre,
                genero,
                hora_funcion,
                duracion,
                entradas_disponibles
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            [
                nombre,
                genero,
                hora_funcion,
                duracion,
                entradas_disponibles
            ]
        )

        pelicula_id = query.rows[0][0]

        return self.find_by_id(pelicula_id)


    def update(self, id, campos):

        campos_validos = {
            key: value
            for key, value in campos.items()
            if key in self.CAMPOS_ACTUALIZABLES
            and value is not None
        }

        if not campos_validos:
            return None

        sets = ", ".join(
            f"{key} = ?"
            for key in campos_validos
        )

        valores = list(campos_validos.values())
        valores.append(id)

        self.client.execute(
            f"""
            UPDATE peliculas
            SET {sets}
            WHERE id = ?
            """,
            valores
        )

        return self.find_by_id(id)

    def delete(self, id):

        pelicula = self.find_by_id(id)

        if pelicula is None:
            return False

        self.client.execute(
            """
            DELETE FROM peliculas
            WHERE id = ?
            """,
            [id]
        )

        return True