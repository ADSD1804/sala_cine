from repositories.pelicula_repository import PeliculaRepository

def test_crear_peliculas():
    repo = PeliculaRepository()

    codigo = "1000"

    pelicula = repo.create(codigo, "Película de prueba", "Acción", "19:00", 120, 50)

    assert pelicula is not None
    assert pelicula["codigo"] == codigo
    assert pelicula["nombre"] == "Película de prueba"
    assert pelicula["genero"] == "Acción"
    assert pelicula["hora_funcion"] == "19:00"
    assert pelicula["duracion"] == 120
    assert pelicula["entradas_disponibles"] == 50

    repo.delete(codigo)

def test_buscar_pelicula():
    repo = PeliculaRepository()
    
    codigo = "1001"
    
    repo.create(codigo, "Pelicula por codigo", "Ficción", "18:00", 100, 50)
    
    pelicula = repo.find_by_code(codigo)
    
    assert pelicula is not None
    assert pelicula["codigo"] == codigo
    assert pelicula["nombre"] == "Pelicula por codigo"
    assert pelicula["genero"] == "Ficción"
    assert pelicula["hora_funcion"] == "18:00"
    assert pelicula["duracion"] == 100
    assert pelicula["entradas_disponibles"] == 50
    
    repo.delete(codigo)

def test_actualizar_pelicula():

    repo = PeliculaRepository()

    codigo = "1002"

    repo.create(codigo, "Pelicula a actualizar", "Acción", "17:00", 100, 60)

    pelicula_actualizada = repo.update(codigo, {"nombre": "Pelicula 5", "genero": "Fantasía"})

    assert pelicula_actualizada is not None
    assert pelicula_actualizada["codigo"] == codigo
    assert pelicula_actualizada["nombre"] == "Pelicula 5"
    assert pelicula_actualizada["genero"] == "Fantasía"
    assert pelicula_actualizada["hora_funcion"] == "17:00"
    assert pelicula_actualizada["duracion"] == 100
    assert pelicula_actualizada["entradas_disponibles"] == 60

    repo.delete(codigo)

def test_borrar_pelicula():

    repo = PeliculaRepository()

    codigo = "2002"

    repo.create(codigo, "Pelicula sin nombre", "Sin genero", "No horario", 0, 0)

    pelicuna_eliminada = repo.delete(codigo)

    assert pelicuna_eliminada is True
    assert repo.find_by_code(codigo) is None

