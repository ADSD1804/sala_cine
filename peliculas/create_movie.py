from pymongo import MongoClient

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")

database = conexion["cine"]

coleccion = database["pelicula"]

def ingresar_pelicula(codigo, nombre, genero, hora_funcion, duracion, entradas_disponibles, precio):

    documento = {
        "codigo": codigo,
        "nombre": nombre,
        "genero": genero,
        "hora_funcion": hora_funcion,
        "duracion": duracion,
        "entradas_disponibles": entradas_disponibles,
        "precio": precio
    }

    coleccion.insert_one(documento)
    