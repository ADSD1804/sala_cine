from pymongo import MongoClient
import tkinter as tk
from tkinter import messagebox
from peliculas.create_movie import ingresar_pelicula
from peliculas.delete_movie import borrar_pelicula

conexion = MongoClient("mongodb+srv://Andredavid:adsd1804@cluster0.zvbp2.mongodb.net/")

database = conexion["cine"]
coleccion = database["pelicula"]

ventana = tk.Tk()
ventana.title("Peliculas")
ventana.geometry("600x600")

tk.Label(ventana, text="Ingresar película").pack

tk.Label(ventana, text="Ingrese el codigo de la pelicula: ").pack()
codigo = tk.Entry(ventana)
codigo.pack()

tk.Label(ventana, text="Ingrese el nombre de la pelicula: ").pack()
nombre = tk.Entry(ventana)
nombre.pack()

tk.Label(ventana, text="Ingrese el genero de la pelicula: ").pack()
genero = tk.Entry(ventana)
genero.pack()

tk.Label(ventana, text="Ingrese la hora de la pelicula: ").pack()
hora_funcion = tk.Entry(ventana)
hora_funcion.pack()

tk.Label(ventana, text="Ingrese la duracion de la pelicula: ").pack()
duracion = tk.Entry(ventana)
duracion.pack()

tk.Label(ventana, text="Ingrese las entradas disponibles de la pelicula: ").pack()
entradas_disponibles = tk.Entry(ventana)
entradas_disponibles.pack()

def crear_pelicula():
    ingresar_pelicula(codigo.get(), nombre.get(), genero.get(), hora_funcion.get(), duracion.get(), entradas_disponibles.get())
    messagebox.showinfo("Pelicula creada", "La pelicula ha sido creada con exito")

def eliminar_pelicula():
    codigo_pelicula = codigo.get()
    borrar_pelicula(codigo_pelicula)
    messagebox.showinfo("Pelicula borrada", "La pelicula ha sido borrada con exito")

boton_eliminar = tk.Button(ventana, text="Borrar Pelicula", command=eliminar_pelicula)
boton_eliminar.pack()

boton_crear = tk.Button(ventana, text="Ingresar Pelicula", command=crear_pelicula)
boton_crear.pack()

ventana.withdraw()

def cerrar_ventana():
    ventana.withdraw()  # Oculta la ventana

boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack()