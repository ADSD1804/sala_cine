from pymongo import MongoClient

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")

database = conexion["cine"]

coleccion = database["usuario"]

def realizar_compra(cedula, nombre_pelicula):
    
    historial_actual = {}
    
    if nombre_pelicula:
        historial_actual["historial_compra"] = nombre_pelicula
        
        
        