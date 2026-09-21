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
    
    pelicula = repo.find_by_codigo(codigo)
    
    assert pelicula is not None
    assert pelicula["codigo"] == codigo
    assert pelicula["nombre"] == "Pelicula por codigo"
    assert pelicula["genero"] == "Ficción"
    assert pelicula["hora_funcion"] == "18:00"
    assert pelicula["duracion"] == 100
    assert pelicula["entradas_disponibles"] == 50
    
    repo.delete(codigo)