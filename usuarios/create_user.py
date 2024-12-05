from pymongo import MongoClient

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")

database = conexion["cine"]

coleccion = database["usuario"]

def ingresar_usuario(cedula, nombre, correo, preferencias):
    historial_compra = []
    
    documento = {
        "cedula": cedula,
        "nombre": nombre,
        "correo": correo,
        "preferencias": preferencias,
        "historial_compra": historial_compra
    }
    
    coleccion.insert_one(documento)
    print("Usuario ingresado con exito!")
    

