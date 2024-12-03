from pymongo import MongoClient

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")

database = conexion["cine"]

coleccion = database["pelicula"]

def borrar_pelicula(codigo):

    resultado = coleccion.delete_one({"codigo":codigo})

    if resultado:
        print("Pelicula borrada con exito!")
    else:
        print("Error al encontrar la pelicula.")