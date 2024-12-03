from pymongo import MongoClient
import tkinter as tk

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")
database = conexion["cine"]
coleccion = database["pelicula"]

ventana = tk.Tk()
ventana.title("Mostrar Peliculas")
ventana.geometry("400x400")

def mostrar_peliculas():
    peliculas = coleccion.find()
    peliculas_texto = ""

    for pelicula in peliculas:
        peliculas_texto += f"Nombre: {pelicula['nombre']}\n"
        peliculas_texto += f"Genero: {pelicula['genero']}\n"
        peliculas_texto += f"Hora de Funcion: {pelicula['hora_funcion']}\n"
        peliculas_texto += f"Duracion: {pelicula['duracion']}\n"
        peliculas_texto += f"Entradas Disponibles: {pelicula['entradas_disponibles']}\n\n"

    ventana_peliculas = tk.Toplevel(ventana)
    ventana_peliculas.title("Peliculas Registradas")
    ventana_peliculas.geometry("400x300")

    texto_peliculas = tk.Text(ventana_peliculas, wrap=tk.WORD)
    texto_peliculas.pack(expand=True, fill=tk.BOTH)

    texto_peliculas.insert(tk.END, peliculas_texto)

    texto_peliculas.config(state=tk.DISABLED)   

boton_mostrarPeliculas = tk.Button(ventana, text="Mostrar Peliculas", command=mostrar_peliculas)
boton_mostrarPeliculas.pack()     
        
ventana.withdraw()

def cerrar_ventana():
    ventana.withdraw()

boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack()


