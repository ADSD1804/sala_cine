from pymongo import MongoClient

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")

database = conexion["cine"]

coleccion = database["usuario"]

def leer_usuario(cedula):
    
    resultado = coleccion.find_one({"cedula":cedula})
    
    if resultado:
        print("Documento de identidad encontrado: ",resultado)
    else:
        print("Error al encontrar el usuario.")
        