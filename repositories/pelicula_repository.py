from db.connection import get_client


class PeliculaRepository:

    CAMPOS_ACTUALIZABLES = {
        "nombre",
        "genero",
        "hora_funcion",
        "duracion",
        "entradas_disponibles",
    }

    def __init__(self):
        self.client = get_client()

    def find_all(self):
        query = self.client.execute("""
            SELECT
                id,
                codigo,
                nombre,
                genero,
                hora_funcion,
                duracion,
                entradas_disponibles
            FROM peliculas
            """)

        return [dict(zip(query.columns, row)) for row in query.rows]

    def find_by_code(self, codigo):
        query = self.client.execute(
            """
            SELECT
                id,
                codigo,
                nombre,
                genero,
                hora_funcion,
                duracion,
                entradas_disponibles
            FROM peliculas
            WHERE codigo = ?
            """,
            [codigo],
        )

        if not query.rows:
            return None

        return dict(zip(query.columns, query.rows[0]))

    def create(
        self, codigo, nombre, genero, hora_funcion, duracion, entradas_disponibles
    ):

        query = self.client.execute(
            """
            INSERT INTO peliculas
            (
                codigo,
                nombre,
                genero,
                hora_funcion,
                duracion,
                entradas_disponibles
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            [codigo, nombre, genero, hora_funcion, duracion, entradas_disponibles],
        )

        return self.find_by_code(codigo)

    def update(self, codigo, campos):

        campos_validos = {
            key: value
            for key, value in campos.items()
            if key in self.CAMPOS_ACTUALIZABLES and value is not None
        }

        if not campos_validos:
            return None

        sets = ", ".join(f"{key} = ?" for key in campos_validos)

        valores = list(campos_validos.values())
        valores.append(codigo)

        self.client.execute(
            f"""
            UPDATE peliculas
            SET {sets}
            WHERE codigo = ?
            """,
            valores,
        )

        return self.find_by_code(codigo)

    def delete(self, codigo):

        pelicula = self.find_by_code(codigo)

        if pelicula is None:
            return False

        self.client.execute(
            """
            DELETE FROM peliculas
            WHERE codigo = ?
            """,
            [codigo],
        )

        return True
