from pymongo import MongoClient

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")

database = conexion["cine"]

coleccion = database["pelicula"]

def leer_pelicula(codigo):
    
    resultado = coleccion.find_one({"codigo":codigo,})
    
    if resultado:
        print("Codigo de pelicula encontrado: ",resultado)
    else:
        print("Error al encontrar el usuario.")
        