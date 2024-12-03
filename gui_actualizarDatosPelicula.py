from pymongo import MongoClient
import tkinter as tk
from tkinter import messagebox

from peliculas.update_movie import actualizar_info_pelicula

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")
database = conexion["cine"]
coleccion = database["pelicula"]

ventana = tk.Tk()
ventana.title("Actualizar Pelicula")
ventana.geometry("500x400")

tk.Label(ventana, text="Actualizar Datos de la Pelicula").pack()

tk.Label(ventana, text="Ingrese el codigo de la pelicula:").pack()
codigo_entry = tk.Entry(ventana)
codigo_entry.pack()

tk.Label(ventana, text="Nuevo Nombre:").pack()
nuevo_nombre_entry = tk.Entry(ventana)
nuevo_nombre_entry.pack()

tk.Label(ventana, text="Nuevo Genero:").pack()
nuevo_genero_entry = tk.Entry(ventana)
nuevo_genero_entry.pack()

tk.Label(ventana, text="Nueva Duracion:").pack()
nuevo_duracion_entry = tk.Entry(ventana)
nuevo_duracion_entry.pack()

tk.Label(ventana, text="Nueva Hora de Función:").pack() 
nueva_hora_entry = tk.Entry(ventana)
nueva_hora_entry.pack()

tk.Label(ventana, text="Nueva entradas disponibles:").pack()
nueva_entradas_entry = tk.Entry(ventana)
nueva_entradas_entry.pack()

def actualizar_pelicula():
    codigo = codigo_entry.get()
    nuevo_nombre = nuevo_nombre_entry.get()
    nuevo_genero = nuevo_genero_entry.get()
    nuevo_duracion = nuevo_duracion_entry.get()
    nueva_hora = nueva_hora_entry.get()
    nueva_entradas = nueva_entradas_entry.get()

    if codigo:  
        actualizar_info_pelicula(codigo, nuevo_nombre if nuevo_nombre else None, nuevo_genero if nuevo_genero else None, nuevo_duracion if nuevo_duracion else None, nueva_hora if nueva_hora else None, nueva_entradas if nueva_entradas else None)
        messagebox.showinfo("Pelicula Actualizada", "La pelicula ha sido actualizada correctamente.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese el codigo de la pelicula.")


tk.Button(ventana, text="Actualizar Pelicula", command= actualizar_pelicula).pack()

def cerrar_ventana():
    ventana.withdraw()

boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack()

ventana.withdraw()