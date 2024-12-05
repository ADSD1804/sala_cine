from pymongo import MongoClient

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")

database = conexion["cine"]

coleccion = database["usuario"]

def actualizar_usuario(cedula, nuevo_nombre = None, nuevo_correo = None, nuevas_preferencias = None):
    
    campos_actuales = {}
    
    if nuevo_nombre:
        campos_actuales["nombre"] = nuevo_nombre
    if nuevo_correo:
        campos_actuales["correo"] = nuevo_correo
    if nuevas_preferencias:
        campos_actuales["preferencias"] = nuevas_preferencias
    if campos_actuales:
        resultado = coleccion.update_one({"cedula":cedula},{"$set":campos_actuales})    
    if resultado.matched_count > 0:
        print("Usuario actualizado exitosamente")
    else:
        print("El usuario no se encontró en la base de datos")
            