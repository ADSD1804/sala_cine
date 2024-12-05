from pymongo import MongoClient

# Conexión a la base de datos
conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")
database = conexion["cine"]
coleccion_usuarios = database["usuario"]
coleccion_peliculas = database["pelicula"]

def comprar_entradas(cedula, nombre_pelicula, cantidad):
    # Verificar si el usuario existe
    usuario = coleccion_usuarios.find_one({"cedula": cedula})
    
    if not usuario:
        print("Error: El usuario no existe.")
        return

    # Buscar la película
    pelicula = coleccion_peliculas.find_one({"nombre": nombre_pelicula})
    
    if not pelicula:
        print("Error: La película no existe.")
        return

    try:
        entradas_disponibles = int(pelicula['entradas_disponibles'])  # Convertir a entero
    except ValueError:
        return "Error: Las entradas disponibles no son un número válido."

    # Verificar si hay suficientes entradas disponibles
    if entradas_disponibles < cantidad:
        print("Error: No hay suficientes entradas disponibles.")
        return

    # Actualizar el historial de compras del usuario
    historial_actual = usuario.get("historial_compra", [])
    historial_actual.append({"pelicula": nombre_pelicula, "cantidad": cantidad})
    
    resultado_actualizacion_usuario = coleccion_usuarios.update_one(
        {"cedula": cedula}, 
        {"$set": {"historial_compra": historial_actual}}
    )
    
    print("Resultado de actualización de usuario:", resultado_actualizacion_usuario.modified_count)

    # Disminuir las entradas disponibles de la película
    nuevas_entradas_disponibles = entradas_disponibles - cantidad
    resultado_actualizacion_pelicula = coleccion_peliculas.update_one(
        {"nombre": nombre_pelicula}, 
        {"$set": {"entradas_disponibles": nuevas_entradas_disponibles}}
    )
    
    print("Resultado de actualización de película:", resultado_actualizacion_pelicula.modified_count)

    if resultado_actualizacion_usuario.modified_count > 0 and resultado_actualizacion_pelicula.modified_count > 0:
        return f"Compra realizada con éxito. Entradas compradas: {cantidad}"
    else:
        return "Error: No se pudo realizar la compra."