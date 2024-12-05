from pymongo import MongoClient

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")

database = conexion["cine"]

coleccion = database["pelicula"]

def actualizar_info_pelicula(codigo, nombre, genero, hora_funcion, duracion, entradas_disponibles):

    campos_actuales = {}

    if nombre:
        campos_actuales["nombre"] = nombre
    if genero:
        campos_actuales["genero"] = genero
    if hora_funcion:
        campos_actuales["hora_funcion"] = hora_funcion
    if duracion:
        campos_actuales["duracion"] = duracion
    if entradas_disponibles:
        campos_actuales["entradas_disponibles"] = entradas_disponibles

    resultado = coleccion.update_one({"codigo": codigo}, {"$set": campos_actuales})

    if resultado.matched_count > 0:
        print("Pelicula actualizada exitosamente")
    else:
        print("La pelicula no se encuentra en la base de datos")

    