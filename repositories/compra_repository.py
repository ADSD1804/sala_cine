from db.connection import get_client


class CompraRepository:

    def __init__(self):
        self.client = get_client()

    def find_all(self):
        query = self.client.execute(""" 
        SELECT *
        FROM compras 
        """)

        return [dict(zip(query.columns, row)) for row in query.rows]

    def find_by_id(self, compra_id):
        query = self.client.execute(
            """
        SELECT *
            FROM compras
            WHERE id = ?
        """,
            [compra_id],
        )

        if not query.rows:
            return None

        return dict(zip(query.columns, query.rows[0]))

    def find_by_usuario(self, usuario_cedula):
        query = self.client.execute(
            """
        SELECT *
        FROM compras 
        WHERE usuario_cedula = ?
        """,
            [usuario_cedula],
        )

        if not query.rows:
            return None

        return dict(zip(query.columns, query.rows[0]))

    def find_by_pelicula(self, pelicula_codigo):
        query = self.client.execute(
            """
        SELECT *
        FROM compras
        WHERE pelicula_codigo = ?
        """,
            [pelicula_codigo],
        )

        return dict(zip(query.columns, query.rows[0]))

    def create(self, usuario_cedula, pelicula_codigo, cantidad, total):
        self.client.execute(
            """ 
        INSERT INTO compras(
        usuario_cedula, 
        pelicula_codigo, 
        cantidad, 
        total) 
        VALUES (?, ?, ?, ?) 
        """,
            [usuario_cedula, pelicula_codigo, cantidad, total],
        )
        query = self.client.execute(
            """
        SELECT *
        FROM compras 
        WHERE usuario_cedula = ? 
        AND pelicula_codigo = ? 
        AND cantidad = ? 
        AND total = ? 
        ORDER BY id DESC LIMIT 1 
        """,
            [usuario_cedula, pelicula_codigo, cantidad, total],
        )

        if not query.rows:
            return None

        return dict(zip(query.columns, query.rows[0]))

    def delete(self, compra_id):
        compra = self.find_by_id(compra_id)

        if compra is None:
            return False

        self.client.execute(
            """
        DELETE
        FROM compras 
        WHERE id = ? 
        """,
            [compra_id],
        )
        return True
