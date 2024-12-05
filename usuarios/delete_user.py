from pymongo import MongoClient

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")

database = conexion["cine"]

coleccion = database["usuario"]

def borrar_usuario(cedula):
    
    resultado = coleccion.delete_one({"cedula":cedula})
    
    if resultado:
        print("Usuario borrado con exito!")
    else:
        print("Error al encontrar el usuario.")